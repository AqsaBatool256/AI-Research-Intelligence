import os

import requests
import streamlit as st


# ============================================================
# BACKEND CONFIGURATION
# ============================================================

try:
    BACKEND_URL = st.secrets["BACKEND_URL"]
except (FileNotFoundError, KeyError):
    BACKEND_URL = os.getenv(
        "BACKEND_URL",
        "http://127.0.0.1:8000",
    )

BACKEND_URL = BACKEND_URL.rstrip("/")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Research Intelligence",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       MAIN BACKGROUND
    ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(59, 130, 246, 0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(139, 92, 246, 0.10),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #050816 0%,
                #0b1020 50%,
                #080b16 100%
            );

        color: #f8fafc;
    }


    /* =========================
       SIDEBAR
    ========================= */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #080c18 0%,
                #0d1324 100%
            );

        border-right:
            1px solid rgba(255, 255, 255, 0.08);
    }


    /* =========================
       MAIN CONTAINER
    ========================= */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* =========================
       HERO
    ========================= */

    .hero {
        padding: 35px;
        border-radius: 24px;
        margin-bottom: 25px;

        background:
            linear-gradient(
                135deg,
                rgba(37, 99, 235, 0.18),
                rgba(124, 58, 237, 0.14)
            );

        border:
            1px solid rgba(148, 163, 184, 0.15);

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.35);

        animation:
            fadeIn 0.8s ease;
    }


    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 10px;

        background:
            linear-gradient(
                90deg,
                #60a5fa,
                #a78bfa,
                #22d3ee
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }


    .hero-subtitle {
        color: #cbd5e1;
        font-size: 1.1rem;
        line-height: 1.7;
        max-width: 900px;
    }


    /* =========================
       GLASS CARDS
    ========================= */

    .glass-card {
        background:
            rgba(15, 23, 42, 0.72);

        border:
            1px solid rgba(148, 163, 184, 0.12);

        border-radius: 20px;

        padding: 22px;

        margin-bottom: 20px;

        box-shadow:
            0 12px 40px rgba(0, 0, 0, 0.25);

        backdrop-filter: blur(12px);

        animation:
            fadeIn 0.7s ease;
    }


    /* =========================
       METRIC CARDS
    ========================= */

    .metric-card {
        background:
            linear-gradient(
                145deg,
                rgba(30, 41, 59, 0.8),
                rgba(15, 23, 42, 0.8)
            );

        border:
            1px solid rgba(148, 163, 184, 0.12);

        border-radius: 18px;

        padding: 20px;

        text-align: center;

        box-shadow:
            0 10px 35px rgba(0, 0, 0, 0.25);

        transition:
            transform 0.25s ease,
            border-color 0.25s ease;
    }


    .metric-card:hover {
        transform: translateY(-5px);

        border-color:
            rgba(96, 165, 250, 0.4);
    }


    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        color: #60a5fa;
    }


    .metric-label {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: 5px;
    }


    /* =========================
       SECTION TITLES
    ========================= */

    .section-title {
        font-size: 1.5rem;
        font-weight: 750;
        color: #f8fafc;

        margin-top: 20px;
        margin-bottom: 15px;
    }


    /* =========================
       DOCUMENT CARDS
    ========================= */

    .document-card {
        background:
            rgba(15, 23, 42, 0.65);

        border:
            1px solid rgba(148, 163, 184, 0.12);

        border-radius: 16px;

        padding: 18px;

        margin-bottom: 12px;

        transition:
            transform 0.25s ease,
            background 0.25s ease;
    }


    .document-card:hover {
        transform: translateX(5px);

        background:
            rgba(30, 41, 59, 0.8);
    }


    .document-name {
        font-weight: 700;
        color: #e2e8f0;
        font-size: 1rem;
    }


    .document-meta {
        color: #94a3b8;
        font-size: 0.85rem;
        margin-top: 5px;
    }


    /* =========================
       SOURCE CARDS
    ========================= */

    .source-card {
        background:
            rgba(30, 41, 59, 0.65);

        border-left:
            3px solid #60a5fa;

        border-radius: 12px;

        padding: 15px;

        margin-top: 10px;

        color: #cbd5e1;

        animation:
            slideUp 0.5s ease;
    }


    .source-header {
        color: #93c5fd;
        font-weight: 700;
        margin-bottom: 7px;
    }


    /* =========================
       STATUS
    ========================= */

    .status-online {
        display: inline-block;

        padding: 6px 12px;

        border-radius: 999px;

        background:
            rgba(34, 197, 94, 0.12);

        border:
            1px solid rgba(34, 197, 94, 0.25);

        color: #86efac;

        font-size: 0.8rem;

        font-weight: 600;
    }


    /* =========================
       BUTTONS
    ========================= */

    .stButton > button {
        border-radius: 12px;

        border:
            1px solid rgba(96, 165, 250, 0.25);

        background:
            linear-gradient(
                135deg,
                #2563eb,
                #7c3aed
            );

        color: white;

        font-weight: 700;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 8px 25px rgba(59, 130, 246, 0.3);
    }


    /* =========================
       ANIMATIONS
    ========================= */

    @keyframes fadeIn {

        from {
            opacity: 0;
            transform: translateY(12px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }

    }


    @keyframes slideUp {

        from {
            opacity: 0;
            transform: translateY(10px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }

    }


    /* =========================
       FOOTER
    ========================= */

    .footer {
        text-align: center;

        color: #64748b;

        padding: 30px 0 10px;

        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# BACKEND FUNCTIONS
# ============================================================


def get_research_stats():
    """Get research knowledge-base statistics."""
    try:
        response = requests.get(
            f"{BACKEND_URL}/research/stats",
            timeout=10,
        )

        if response.status_code == 200:
            return response.json()

    except requests.exceptions.RequestException:
        pass

    return {
        "documents": 0,
        "pages": 0,
        "chunks": 0,
    }


def get_indexed_documents():
    """Get indexed research documents."""
    try:
        response = requests.get(
            f"{BACKEND_URL}/research/documents",
            timeout=10,
        )

        if response.status_code == 200:
            return response.json().get(
                "documents",
                [],
            )

    except requests.exceptions.RequestException:
        pass

    return []


def upload_document(uploaded_file):
    """Upload and index a PDF."""
    try:
        response = requests.post(
            f"{BACKEND_URL}/research/upload",
            files={
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    "application/pdf",
                )
            },
            timeout=120,
        )

        if response.status_code == 200:
            return response.json()

        try:
            return {"error": response.json()}
        except Exception:
            return {"error": response.text}

    except requests.exceptions.RequestException as error:
        return {"error": str(error)}


def ask_research_question(question):
    """Ask a question about indexed research."""
    try:
        response = requests.get(
            f"{BACKEND_URL}/research/ask",
            params={"question": question},
            timeout=120,
        )

        if response.status_code == 200:
            return response.json()

        try:
            return {"error": response.json()}
        except Exception:
            return {"error": response.text}

    except requests.exceptions.RequestException as error:
        return {"error": str(error)}


# ============================================================
# LOAD CURRENT DATA
# ============================================================

stats = get_research_stats()

indexed_documents = get_indexed_documents()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown(
        """
        <div style="
            text-align:center;
            padding:15px 0 25px;
        ">

            <div style="
                font-size:3rem;
            ">
                🧠
            </div>

            <h2 style="
                margin-bottom:5px;
            ">
                Research AI
            </h2>

            <p style="
                color:#94a3b8;
                font-size:0.9rem;
            ">
                Intelligence Platform
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<span class="status-online">● Platform Ready</span>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### ⚙️ System")

    st.caption(f"Backend: `{BACKEND_URL}`")

    st.caption("FastAPI + Gemini + ChromaDB")

    st.markdown("---")

    st.markdown("### 🚀 Capabilities")

    st.markdown(
        """
        - 📄 PDF Research Analysis
        - 🔎 Semantic Search
        - 🤖 AI Research Answers
        - 📚 Multi-Document Knowledge Base
        - 📑 Page-Level Sources
        - 📊 Knowledge Statistics
        """
    )


# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-title">
            🧠 AI Research Intelligence Platform
        </div>

        <div class="hero-subtitle">
            Transform research papers and technical documents
            into an intelligent, searchable knowledge base.
            Upload PDFs, ask questions, and receive grounded
            AI answers with traceable document and page sources.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# METRICS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-value">
                {stats.get("documents", 0)}
            </div>

            <div class="metric-label">
                Research Documents
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:
    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-value">
                {stats.get("pages", 0)}
            </div>

            <div class="metric-label">
                Indexed Pages
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with col3:
    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-value">
                {stats.get("chunks", 0)}
            </div>

            <div class="metric-label">
                Knowledge Chunks
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("")


# ============================================================
# PDF UPLOAD
# ============================================================

st.markdown(
    '<div class="section-title">📄 Add Research Document</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="glass-card">

        <p style="color:#94a3b8;">
            Upload a research paper, technical report,
            academic document, or other text-based PDF.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"],
    help=("Upload a research PDF to extract, index, and search its content."),
)


if uploaded_file is not None:
    if st.button(
        "🚀 Analyze & Index Document",
        use_container_width=True,
    ):
        with st.spinner("Extracting, chunking, and indexing your research document..."):
            result = upload_document(uploaded_file)

        if "error" in result:
            st.error(f"Upload failed: {result['error']}")

        else:
            st.success("Research document indexed successfully!")

            st.session_state["last_upload"] = result

            st.rerun()


# ============================================================
# LAST UPLOAD
# ============================================================

if "last_upload" in st.session_state:
    last_upload = st.session_state["last_upload"]

    st.markdown(
        '<div class="section-title">✅ Last Indexed Document</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="glass-card">

            <h3 style="margin-bottom:8px;">
                📄 {last_upload.get("document", "Unknown")}
            </h3>

            <p style="
                color:#94a3b8;
                margin-bottom:0;
            ">
                {last_upload.get("pages", 0)} pages
                •
                {last_upload.get("chunks", 0)} knowledge chunks
                •
                Successfully indexed
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# DOCUMENT LIBRARY
# ============================================================

st.markdown(
    '<div class="section-title">📚 Research Document Library</div>',
    unsafe_allow_html=True,
)


if indexed_documents:
    for document in indexed_documents:
        st.markdown(
            f"""
            <div class="document-card">

                <div class="document-name">
                    📄 {document.get("document", "Unknown")}
                </div>

                <div class="document-meta">
                    {document.get("pages", 0)} pages
                    •
                    {document.get("status", "Unknown")}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

else:
    st.info("No research documents have been indexed yet.")


# ============================================================
# RESEARCH ASSISTANT
# ============================================================

st.markdown(
    '<div class="section-title">🤖 Research Assistant</div>',
    unsafe_allow_html=True,
)


question = st.text_area(
    "Ask a question about your uploaded research",
    placeholder=("Example: What are the main findings of the research?"),
    height=120,
)


if st.button(
    "🔎 Ask Research Assistant",
    use_container_width=True,
):
    if not question.strip():
        st.warning("Please enter a research question.")

    elif stats.get("documents", 0) == 0:
        st.warning("Please upload and index at least one research document first.")

    else:
        with st.spinner(
            "Searching the research knowledge base and generating an answer..."
        ):
            result = ask_research_question(question.strip())

        if "error" in result:
            st.error(f"Research request failed: {result['error']}")

        else:
            st.markdown("### 💡 AI Answer")

            st.markdown(
                f"""
                <div class="glass-card">

                    <div style="
                        font-size:1.05rem;
                        line-height:1.8;
                        color:#e2e8f0;
                    ">
                        {result.get("answer", "No answer returned.")}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            sources = result.get(
                "sources",
                [],
            )

            if sources:
                st.markdown("### 📑 Research Sources")

                for source in sources:
                    st.markdown(
                        f"""
                        <div class="source-card">

                            <div class="source-header">
                                📄 {source.get("document", "Unknown")}
                                • Page {source.get("page", "?")}
                            </div>

                            <div>
                                {source.get("text", "")}
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

            else:
                st.info("No source passages were returned.")


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        AI Research Intelligence Platform

        •

        Built with Python, Streamlit, FastAPI,
        ChromaDB, PyMuPDF & Gemini

        <br><br>

        Developed by
        <strong>
            Aqsa Batool Saqib
        </strong>

    </div>
    """,
    unsafe_allow_html=True,
)
