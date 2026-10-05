import requests
import streamlit as st


BACKEND_URL = "http://127.0.0.1:8000"


# =========================
# BACKEND HELPERS
# =========================


def get_research_stats():
    """Fetch current research knowledge base statistics."""

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
    """Fetch indexed research documents."""

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


stats = get_research_stats()
indexed_documents = get_indexed_documents()


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="ResearchAI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================
# CUSTOM STYLES
# =========================

st.html(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99, 102, 241, 0.16),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(168, 85, 247, 0.14),
                transparent 30%
            ),
            #080b14;

        color: #f8fafc;
    }


    #MainMenu {
        visibility: hidden;
    }


    footer {
        visibility: hidden;
    }


    .block-container {
        max-width: 1400px;

        padding-top: 2rem;

        padding-bottom: 3rem;
    }


    section[data-testid="stSidebar"] {
        background: #0b1020;

        border-right:
            1px solid
            rgba(148, 163, 184, 0.12);
    }


    /* =========================
       HERO
       ========================= */

    .hero-icon {
        font-size: 3.5rem;

        animation:
            floating
            4s
            ease-in-out
            infinite;

        margin-bottom: 0.5rem;
    }


    @keyframes floating {

        0% {
            transform:
                translateY(0px);
        }

        50% {
            transform:
                translateY(-10px);
        }

        100% {
            transform:
                translateY(0px);
        }
    }


    .hero-title {

        font-size: 3.2rem;

        font-weight: 800;

        line-height: 1.1;

        letter-spacing: -1px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #a5b4fc,
                #c084fc
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;

        margin-bottom: 0.5rem;
    }


    .hero-subtitle {

        color: #94a3b8;

        font-size: 1.15rem;

        margin-bottom: 2rem;
    }


    /* =========================
       METRIC CARDS
       ========================= */

    .metric-card {

        background:
            rgba(
                15,
                23,
                42,
                0.78
            );

        border:
            1px solid
            rgba(
                148,
                163,
                184,
                0.13
            );

        border-radius: 18px;

        padding: 1.35rem;

        min-height: 125px;

        transition:
            all
            0.3s
            ease;

        box-sizing: border-box;
    }


    .metric-card:hover {

        transform:
            translateY(-6px);

        border-color:
            rgba(
                129,
                140,
                248,
                0.55
            );

        box-shadow:
            0 15px 40px
            rgba(
                79,
                70,
                229,
                0.18
            );
    }


    .metric-icon {

        font-size: 1.8rem;

        margin-bottom: 0.35rem;
    }


    .metric-value {

        font-size: 1.8rem;

        font-weight: 750;

        color: #f8fafc;
    }


    .metric-label {

        color: #94a3b8;

        font-size: 0.9rem;

        margin-top: 0.15rem;
    }


    /* =========================
       SECTIONS
       ========================= */

    .section-title {

        font-size: 1.5rem;

        font-weight: 700;

        color: #f8fafc;

        margin-top: 2rem;

        margin-bottom: 0.8rem;
    }


    /* =========================
       UPLOAD CARD
       ========================= */

    .upload-card {

        background:
            linear-gradient(
                135deg,
                rgba(
                    30,
                    41,
                    59,
                    0.82
                ),
                rgba(
                    15,
                    23,
                    42,
                    0.72
                )
            );

        border:
            1px dashed
            rgba(
                129,
                140,
                248,
                0.55
            );

        border-radius: 22px;

        padding: 2rem;

        text-align: center;

        margin-bottom: 1rem;

        transition:
            all
            0.3s
            ease;
    }


    .upload-card:hover {

        border-color:
            rgba(
                192,
                132,
                252,
                0.8
            );

        box-shadow:
            0 15px 45px
            rgba(
                99,
                102,
                241,
                0.12
            );

        transform:
            translateY(-2px);
    }


    .upload-icon {

        font-size: 3.5rem;

        margin-bottom: 0.7rem;
    }


    .upload-title {

        font-size: 1.3rem;

        font-weight: 700;

        color: #f8fafc;

        margin-bottom: 0.4rem;
    }


    .upload-description {

        color: #94a3b8;

        font-size: 0.95rem;

        line-height: 1.6;
    }


    /* =========================
       DOCUMENT CARDS
       ========================= */

    .document-card {

        background:
            rgba(
                15,
                23,
                42,
                0.78
            );

        border:
            1px solid
            rgba(
                148,
                163,
                184,
                0.13
            );

        border-radius: 18px;

        padding: 1.2rem;

        margin-bottom: 0.8rem;

        transition:
            all
            0.3s
            ease;
    }


    .document-card:hover {

        transform:
            translateY(-4px);

        border-color:
            rgba(
                129,
                140,
                248,
                0.45
            );

        box-shadow:
            0 12px 35px
            rgba(
                79,
                70,
                229,
                0.12
            );
    }


    .document-name {

        font-size: 1.05rem;

        font-weight: 700;

        color: #f8fafc;

        margin-bottom: 0.45rem;
    }


    .document-meta {

        color: #94a3b8;

        font-size: 0.9rem;
    }


    .document-status {

        color: #86efac;

        font-size: 0.9rem;

        font-weight: 600;
    }


    /* =========================
       ASSISTANT
       ========================= */

    .assistant-card {

        background:
            rgba(
                15,
                23,
                42,
                0.72
            );

        border:
            1px solid
            rgba(
                148,
                163,
                184,
                0.12
            );

        border-radius: 20px;

        padding: 1.5rem;

        margin-top: 0.5rem;

        color: #f8fafc;
    }


    .assistant-description {

        color: #94a3b8;

        line-height: 1.6;

        margin-top: 0.5rem;
    }


    /* =========================
       SOURCE CARDS
       ========================= */

    .source-card {

        background:
            rgba(
                15,
                23,
                42,
                0.72
            );

        border:
            1px solid
            rgba(
                129,
                140,
                248,
                0.18
            );

        border-radius: 14px;

        padding: 1rem;

        margin-bottom: 0.8rem;
    }


    .source-title {

        font-weight: 700;

        color: #e2e8f0;
    }


    .source-page {

        color: #a5b4fc;

        font-size: 0.9rem;

        margin-top: 0.25rem;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer-text {

        text-align: center;

        color: #64748b;

        font-size: 0.85rem;

        margin-top: 1.5rem;
    }

    </style>
    """
)


# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.markdown("## 🧠 ResearchAI")

    st.caption("AI Research Intelligence Platform")

    st.divider()

    st.markdown("### Navigation")

    st.button(
        "📊 Dashboard",
        use_container_width=True,
    )

    st.button(
        "📄 Documents",
        use_container_width=True,
    )

    st.button(
        "💬 Research Assistant",
        use_container_width=True,
    )

    st.button(
        "📈 Research Insights",
        use_container_width=True,
    )

    st.divider()

    st.markdown("### Platform")

    st.caption(
        "Upload research papers and transform "
        "them into searchable AI-powered knowledge."
    )


# =========================
# HERO
# =========================

st.html(
    """
    <div class="hero-icon">
        🧠
    </div>

    <div class="hero-title">
        Research Intelligence Platform
    </div>

    <div class="hero-subtitle">
        Transform research papers into searchable,
        AI-powered knowledge.
    </div>
    """
)


# =========================
# DASHBOARD METRICS
# =========================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.html(
        f"""
        <div class="metric-card">

            <div class="metric-icon">
                📄
            </div>

            <div class="metric-value">
                {stats["documents"]}
            </div>

            <div class="metric-label">
                Documents
            </div>

        </div>
        """
    )


with col2:
    st.html(
        f"""
        <div class="metric-card">

            <div class="metric-icon">
                📑
            </div>

            <div class="metric-value">
                {stats["pages"]}
            </div>

            <div class="metric-label">
                Pages Indexed
            </div>

        </div>
        """
    )


with col3:
    st.html(
        f"""
        <div class="metric-card">

            <div class="metric-icon">
                🧩
            </div>

            <div class="metric-value">
                {stats["chunks"]}
            </div>

            <div class="metric-label">
                Knowledge Chunks
            </div>

        </div>
        """
    )


with col4:
    st.html(
        """
        <div class="metric-card">

            <div class="metric-icon">
                ✨
            </div>

            <div class="metric-value">
                AI
            </div>

            <div class="metric-label">
                Research Engine
            </div>

        </div>
        """
    )


# =========================
# DOCUMENT UPLOAD
# =========================

st.html(
    """
    <div class="section-title">
        📚 Add Research Documents
    </div>

    <div class="upload-card">

        <div class="upload-icon">
            📄
        </div>

        <div class="upload-title">
            Build your research knowledge base
        </div>

        <div class="upload-description">
            Upload PDF research papers, reports,
            theses, or technical documents.
        </div>

    </div>
    """
)


uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"],
)


if uploaded_file is not None:
    st.info(f"📄 Selected: {uploaded_file.name}")

    if st.button(
        "⚡ Index Research Document",
        type="primary",
        use_container_width=True,
    ):
        with st.spinner("Extracting, chunking, and indexing your research paper..."):
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
                    result = response.json()

                    st.success("✅ Research document indexed successfully!")

                    st.session_state["last_upload"] = result

                    st.rerun()

                else:
                    st.error(f"❌ Upload failed (HTTP {response.status_code})")

                    st.code(response.text)

            except requests.exceptions.ConnectionError:
                st.error(
                    "❌ Could not connect to the ResearchAI "
                    "backend. Make sure FastAPI is running "
                    "on http://127.0.0.1:8000."
                )

            except requests.exceptions.Timeout:
                st.error(
                    "⏳ The backend took too long to process the research document."
                )

            except requests.exceptions.RequestException as error:
                st.error("❌ An error occurred while uploading the document.")

                st.code(str(error))


# =========================
# LAST UPLOAD
# =========================

if "last_upload" in st.session_state:
    result = st.session_state["last_upload"]

    st.success(f"📚 {result['document']} is ready for research.")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric(
            "Pages",
            result["pages"],
        )

    with result_col2:
        st.metric(
            "Knowledge Chunks",
            result["chunks"],
        )

    with result_col3:
        st.metric(
            "Status",
            "Indexed",
        )


# =========================
# DOCUMENT LIBRARY
# =========================

st.html(
    """
    <div class="section-title">
        📂 Indexed Research Documents
    </div>
    """
)


if indexed_documents:
    for document in indexed_documents:
        document_col1, document_col2 = st.columns([4, 1])

        with document_col1:
            st.html(
                f"""
                <div class="document-card">

                    <div class="document-name">
                        📄 {document["document"]}
                    </div>

                    <div class="document-meta">
                        {document["pages"]} page(s)
                    </div>

                </div>
                """
            )

        with document_col2:
            st.html(
                f"""
                <div class="document-card">

                    <div class="document-status">
                        🟢 {document["status"]}
                    </div>

                </div>
                """
            )

else:
    st.info("No research documents have been indexed yet.")


# =========================
# RESEARCH ASSISTANT
# =========================

st.html(
    """
    <div class="section-title">
        💬 Ask Your Research
    </div>

    <div class="assistant-card">

        <strong>
            Ask questions about your research documents
        </strong>

        <div class="assistant-description">

            ResearchAI retrieves relevant passages and
            generates grounded answers with source citations.

        </div>

    </div>
    """
)


question = st.text_input(
    "Research question",
    placeholder=("Example: What methodology does this research paper use?"),
)


if st.button(
    "🔍 Analyze Research",
    type="primary",
    use_container_width=True,
):
    if not question.strip():
        st.warning("Please enter a research question.")

    else:
        with st.spinner("Searching your research knowledge base..."):
            try:
                response = requests.get(
                    f"{BACKEND_URL}/research/ask",
                    params={"question": question},
                    timeout=120,
                )

                if response.status_code == 200:
                    result = response.json()

                    st.markdown("### 💡 Research Answer")

                    st.write(result["answer"])

                    sources = result.get("sources", [])

                    if sources:
                        st.markdown("### 📚 Sources")

                        for source in sources:
                            st.html(
                                f"""
                                <div class="source-card">

                                    <div class="source-title">
                                        📄 {source["document"]}
                                    </div>

                                    <div class="source-page">
                                        Page {source["page"]}
                                    </div>

                                </div>
                                """
                            )

                else:
                    st.error(
                        f"❌ Research request failed (HTTP {response.status_code})"
                    )

                    st.code(response.text)

            except requests.exceptions.ConnectionError:
                st.error(
                    "❌ Could not connect to the ResearchAI "
                    "backend. Make sure FastAPI is running."
                )

            except requests.exceptions.Timeout:
                st.error("⏳ The research request took too long.")

            except requests.exceptions.RequestException as error:
                st.error("❌ An error occurred while contacting the research engine.")

                st.code(str(error))


# =========================
# FOOTER
# =========================

st.divider()


st.html(
    """
    <div class="footer-text">
        ResearchAI • Powered by RAG + ChromaDB + Gemini
    </div>
    """
)
