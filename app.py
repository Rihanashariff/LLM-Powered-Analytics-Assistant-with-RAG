import streamlit as st
from llm.router import route_query
from sql.nl_to_sql import generate_sql, execute_sql, summarize
from rag.retriever import retrieve
from llm.sentiment import analyze_reviews
from llm.synthesizer import synthesize
from llm.chart_generator import generate_chart

st.title("LLM Analytics Assistant with RAG")

query = st.text_input("Ask your question")

if st.button("Submit"):

    route = route_query(query)

    if route == "SQL":
        sql = generate_sql(query)
        df = execute_sql(sql)

        st.write(df)

        summary = summarize(df)
        st.write(summary)

        chart = generate_chart(df)
        if chart:
            st.plotly_chart(chart)

    elif route == "RAG":
        chunks = retrieve(query)
        result = analyze_reviews(chunks)
        st.write(result)

    else:
        sql = generate_sql(query)
        df = execute_sql(sql)
        sql_summary = summarize(df)

        chunks = retrieve(query)
        rag_result = analyze_reviews(chunks)

        final = synthesize(sql_summary, rag_result)
        st.write(final)