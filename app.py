import streamlit as st
from databricks.sdk import WorkspaceClient
import time

st.title("Execute sample.py")

w = WorkspaceClient()

JOB_ID = 473566736965506

if st.button("Run SampleJob"):
    run = w.jobs.run_now(job_id=JOB_ID)

    run_id = run.run_id
    st.write(f"Run ID: {run_id}")

    with st.spinner("Execution under progress..."):
        while True:
            job_run = w.jobs.get_run(run_id)
            state = job_run.state.life_cycle_state

            if state == "TERMINATED":
                break

            time.sleep(3)

    output = w.jobs.get_run_output(run_id)

    st.success("Finished executing sample.py")
    st.write(output)
