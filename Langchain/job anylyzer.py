import os
from pathlib import Path
from typing import Dict, Any, List
import PyPDF2
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel, Field

# ===== STEP 1: Load environment variables from .env file =====
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# ===== STEP 2: Define output schema =====
class ResumeAnalysis(BaseModel):
    candidate_name: str = Field(description="Candidate's full name")
    match_score: int = Field(description="Match score between 0-100")
    key_skills: list[str] = Field(description="List of key skills from resume")
    experience_years: float = Field(description="Total years of experience")
    strengths: list[str] = Field(description="Candidate's strengths for this role")
    gaps: list[str] = Field(description="Missing skills/experience")
    feedback: str = Field(description="Detailed feedback and recommendations")
    recommendation: str = Field(description="Recommended, Potential, or Not Recommended")

# ===== STEP 3: Text extraction functions =====
def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF resume"""
    text = ""
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text.strip()

def extract_text_from_file(file_path: str) -> str:
    """Extract text from text file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().strip()

def extract_resume_text(resume_path: str) -> str:
    """Main extraction function that handles PDF or text"""
    if resume_path.endswith('.pdf'):
        return extract_text_from_pdf(resume_path)
    elif resume_path.endswith('.txt'):
        return extract_text_from_file(resume_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or TXT.")

# ===== STEP 4: Validation function =====
def validate_inputs(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Validate that resume and job description exist"""
    if not inputs.get("resume_text") or not inputs.get("resume_text").strip():
        raise ValueError("Resume text is empty")
    if not inputs.get("job_description") or not inputs.get("job_description").strip():
        raise ValueError("Job description is empty")
    return inputs

# ===== STEP 5: Build the LangChain pipeline (FIXED) =====
# ===== STEP 5: Build the LangChain pipeline =====

# Paste your actual secret key directly between the quotes below
MY_REAL_API_KEY = "AQ.Ab8RN6JtIDlz4V_VtIcNGhxCPWNOGaXQ2CbhJhzRFQfNLp-hmQ" 

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",          # FIX: Changed from 3.5 to a valid production model
    temperature=0.0,
    google_api_key=MY_REAL_API_KEY  # FIX: Explicitly passing your pasted key variable
)

# Keep the rest of your Step 5 code exactly the same
structured_llm = llm.with_structured_output(ResumeAnalysis)

# CLEANED: Prompt instructions relying cleanly on Pydantic's schema rules
prompt_template = ChatPromptTemplate.from_template(
    """You are an expert recruiter analyzing a resume against a job description.
    
    JOB DESCRIPTION:
    {job_description}
    
    RESUME:
    {resume_text}
    
    Analyze this resume considering skills match, experience relevance, education fit, and overall alignment."""
)

# FIXED: Chain pipeline passes data directly to structured_llm
analysis_chain_with_schema = (
    RunnableLambda(lambda inputs: validate_inputs(inputs))
    | RunnableLambda(lambda inputs: {
        "resume_text": inputs["resume_text"],
        "job_description": inputs["job_description"]
    })
    | prompt_template
    | structured_llm
)

# ===== STEP 6: Main analysis function =====
def analyze_resume(resume_path: str, job_description: str) -> ResumeAnalysis:
    """Main function to analyze a single resume against a job description"""
    resume_text = extract_resume_text(resume_path)
    inputs = {
        "resume_text": resume_text,
        "job_description": job_description
    }
    return analysis_chain_with_schema.invoke(inputs)

# ===== STEP 7: Bulk Processing & Ranking Function (NEW) =====
def analyze_and_rank_folder(folder_path: str, job_description: str) -> List[Dict[str, Any]]:
    """Analyzes all PDFs/TXT files in a folder and returns them ranked by match score"""
    path = Path(folder_path)
    if not path.exists() or not path.is_dir():
        raise FileNotFoundError(f"Directory '{folder_path}' does not exist.")
        
    supported_extensions = {'.pdf', '.txt'}
    results = []
    
    print(f"📂 Scanning folder '{folder_path}' for resumes...")
    
    for file in path.iterdir():
        if file.suffix.lower() in supported_extensions:
            print(f"⏳ Analyzing: {file.name}...")
            try:
                analysis = analyze_resume(str(file), job_description)
                results.append({
                    "file_name": file.name,
                    "analysis": analysis,
                    "score": analysis.match_score
                })
            except Exception as e:
                print(f"❌ Skipped {file.name} due to an error: {e}")
                
    # Sort results in descending order by score
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

# ===== STEP 8: Display results =====
def display_analysis(analysis: ResumeAnalysis):
    """Format and display a single analysis report"""
    print("\n" + "="*60)
    print("📋 RESUME ANALYSIS REPORT")
    print("="*60)
    print(f"\n👤 Candidate: {analysis.candidate_name}")
    print(f"\n🎯 Match Score: {analysis.match_score}/100")
    score_icon = "🟢" if analysis.match_score >= 80 else "🟡" if analysis.match_score >= 60 else "🔴"
    print(f"{score_icon} Recommendation: {analysis.recommendation}")
    print(f"\n⏱ Experience: {analysis.experience_years} years")
    print("\n🛠 Key Skills Identified:")
    for skill in analysis.key_skills:
        print(f" • {skill}")
    print("\n💪 Strengths for This Role:")
    for strength in analysis.strengths:
        print(f" • {strength}")
    print("\n⚠️ Missing Skills/Gaps:")
    for gap in analysis.gaps:
        print(f" • {gap}")
    print(f"\n📝 Detailed Feedback:\n{analysis.feedback}")
    print("\n" + "="*60)

def display_leaderboard(ranked_results: List[Dict[str, Any]]):
    """Format and display a clean summary leaderboard of candidates"""
    print("\n" + "🏆" * 25)
    print("   CANDIDATE RANKING LEADERBOARD")
    print("🏆" * 25)
    print(f"{'Rank':<6}{'Candidate Name':<25}{'Score':<8}{'Recommendation':<15}")
    print("-" * 60)
    
    for rank, item in enumerate(ranked_results, 1):
        analysis = item["analysis"]
        print(f"{rank:<6}{analysis.candidate_name:<25}{analysis.match_score:<8}{analysis.recommendation:<15}")
    print("=" * 60 + "\n")

# ===== STEP 9: Example usage =====
if __name__ == "__main__":
    job_desc = """
    Senior Software Engineer Position Requirements:
    - 5+ years of software development experience
    - Strong proficiency in Python, JavaScript
    - Experience with cloud platforms (AWS, Azure)
    - Knowledge of machine learning frameworks
    - Bachelor's degree in Computer Science or related field
    """
    
    # Mode Toggle: Set to True to analyze a full folder, False for a single file
    RUN_BULK_FOLDER_ANALYSIS = True
    
    if RUN_BULK_FOLDER_ANALYSIS:
        # Create a folder named 'resumes' and place your target files inside it
        target_folder = "./resumes"
        
        # Helper to dynamically build folder for easy local testing
        os.makedirs(target_folder, exist_ok=True)
        
        try:
            ranked_candidates = analyze_and_rank_folder(target_folder, job_desc)
            
            if not ranked_candidates:
                print(f"ℹ️ No resumes found in '{target_folder}'. Drop some .pdf or .txt files inside.")
            else:
                # 1. Show summary list
                display_leaderboard(ranked_candidates)
                
                # 2. Print out full analysis details for the #1 top matching profile
                print("🌟 Top Choice Candidate Deep Dive:")
                display_analysis(ranked_candidates[0]["analysis"])
                
        except Exception as e:
            print(f"❌ System Error: {e}")
            
    else:
        # Single file analysis fallback
        single_resume = "resume.pdf"
        try:
            result = analyze_resume(single_resume, job_desc)
            display_analysis(result)
        except FileNotFoundError:
            print("❌ Single resume file not found.")
        except Exception as e:
            print(f"❌ Error: {e}")
