import streamlit as st
import requests

st.title("Voice to Code Generator")
real_text = ""
audio = st.audio_input("Record your voice")

if audio is not None:
    st.write("Processing...")

    audio_bytes = audio.getvalue()

    response = requests.post(
        "http://127.0.0.1:8000/speech-to-text",
        data=audio_bytes,
        headers={"Content-Type": "application/octet-stream"}
    )

    if response.status_code == 200:
        st.write("Transcription:", response.json()["transcription"])
        real_text = response.json()["transcription"]
        
        
        
        
        st.subheader("Code")

        response = requests.get(
            "http://127.0.0.1:8000/generate-response",
            params = {
            "prompt": f"""<|begin_of_text|>
        <|system|>
        You are a code generation engine inside a software system.

        Your sole responsibility is to generate source code based on a user’s programming instruction.

        SYSTEM CONTEXT:
        - The user’s instruction comes from speech-to-text transcription.
        - The instruction may be short, informal, or imperfectly phrased.
        - You must infer reasonable intent, but you must NOT invent requirements.

        RULES (STRICT, NON-NEGOTIABLE):

        -ALL THE SOLUTIONS SHOULD BE IN C++ PROGRAMMING LANGUAGE
        - Do NOT include test cases unless explicitly requested.
        - Do NOT include multiple solutions.
        - Do NOT ask clarifying questions.
        - Do NOT mention assumptions unless asked.
        - Generated code must be syntactically valid.
        - Generated code must be minimal and idiomatic.

        ERROR HANDLING:
        - DO NOT ANSWER IF THE INSTRUCTION IS NOT A PROGRAMMING INSTRUCTION, Do not even generate comments.
        - If the instruction is random or nonsensical, do not generate response.
        - If the instruction is random questions, do not generate response.
        - If the instruction is ambiguous, return "Give better instructions".
        - If the instruction is invalid or impossible, output a single-line comment explaining the issue.

        SECURITY:
        - Do NOT generate code that performs destructive actions unless explicitly requested.


        ALSO THE GENERATED CODE MUST BE IN THE FORMAT SO THAT IT CAN BE COPIED AND PASTED DIRECTLY INTO A FILE WITHOUT MODIFICATION.
        <|end_of_system|>

        <|user|>
        {real_text}
        <|end_of_user|>

        <|assistant|>
        """
        }
        )

        if response.status_code == 200:
            st.write(response.json()["response"])
        else:
            st.error("Error generating response")
                
        
        
        
        
        
    else:
        st.error("Error processing audio")
        
