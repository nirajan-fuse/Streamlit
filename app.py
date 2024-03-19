import streamlit as st
import pandas as pd

st.sidebar.title("Pages")
page = st.sidebar.selectbox("Select Page", ["Employee", "Department", "Joined Data"])

if page == "Employee":
    df = pd.read_csv("employee_data.csv", index_col=0)
    st.write(df)
    st.title("Employee data entry: ")
    emp_id = st.number_input(
        "Employee ID: ",
        value=None,
        min_value=1,
        step=1,
        placeholder="Enter Employee ID",
    )
    emp_name = st.text_input("Employee Name: ", placeholder="Enter Employee name")
    emp_job = st.text_input("Employee Job: ", placeholder="Enter Employee job")
    emp_dept_num = st.number_input(
        "Employee Depart number: ",
        value=None,
        min_value=1,
        step=1,
        placeholder="Enter Employee Dept number",
    )
    if st.button("Submit"):
        if all(var is not None for var in [emp_id, emp_name, emp_job, emp_dept_num]):
            if emp_id not in df["Empno"].values:
                new_data = {
                    "Empno": emp_id,
                    "Ename": emp_name,
                    "Job": emp_job,
                    "Deptno": emp_dept_num,
                }
                new_data = pd.DataFrame([new_data])
                df = pd.concat([df, new_data])
                df = df.reset_index(drop=True)
                df.to_csv("employee_data.csv")
                st.success("Data submitted")
            else:
                st.error("Employee ID already exists")
        else:
            st.error("Please enter all the required data")
elif page == "Department":
    df = pd.read_csv("department_data.csv", index_col=0)
    st.write(df)
    st.title("Department data entry: ")
    dept_id = st.number_input(
        "Department ID: ",
        value=None,
        min_value=1,
        step=1,
        placeholder="Enter Department ID",
    )
    dept_name = st.text_input("Department Name: ", placeholder="Enter Employee name")
    dept_add = st.text_input(
        "Department Location: ", placeholder="Enter Department location"
    )
    if st.button("Submit"):
        if all(var is not None for var in [dept_id, dept_name, dept_add]):
            if dept_id not in df["Deptno"].values:
                new_data = {"Deptno": dept_id, "dname": dept_name, "loc": dept_add}
                new_data = pd.DataFrame([new_data])
                df = pd.concat([df, new_data])
                df = df.reset_index(drop=True)
                df.to_csv("department_data.csv")
                st.success("Data submitted")
            else:
                st.error("Department ID already exists")
        else:
            st.error("Please enter all the required data")
else:
    st.header("Visualize Data")
    employee_data = pd.read_csv("employee_data.csv", index_col=0)
    department_data = pd.read_csv("department_data.csv", index_col=0)

    joined_data = pd.merge(employee_data, department_data, on="Deptno", how="outer")
    st.write(joined_data[["Empno", "Ename", "Deptno", "dname"]])
