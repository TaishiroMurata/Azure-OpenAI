""" with st.chat_message("assistant"):
        chat = ChatOpenAI(
            model_name=os.environ["OPEN_AI_MODEL"],
            temperature=os.environ["OPENAI_API_TEMPERATURE"],
        )
        messages = [HumanMessage(content=prompt)]
        response = chat(messages)
        st.markdown(response.content) """