# Creates samples 
import pandas as pd

# Define the data for each glossary
project_glossary_data = [
    {
        "Nick Name": "Project_Management_Scope_Creep",
        "Name": "Scope Creep",
        "Status": "Draft",
        "Definition": "Uncontrolled changes or continuous growth in a project's scope.",
        "Acronym": "SC",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Change_Control;Project_Management_Scope_Change@otherGlossaryName;",
        "Synonyms": "Project_Management_Scope_Expansion;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Gantt_Chart",
        "Name": "Gantt Chart",
        "Status": "Approved",
        "Definition": "A type of bar chart that illustrates a project schedule.",
        "Acronym": "GC",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Timeline;Project_Management_Schedule@otherGlossaryName;",
        "Synonyms": "Project_Management_Bar_Chart;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Risk_Assessment",
        "Name": "Risk Assessment",
        "Status": "Approved",
        "Definition": "The process of identifying and analyzing potential issues that could negatively impact key business initiatives or projects.",
        "Acronym": "RA",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Risk_Management;Project_Management_Risk_Analysis@otherGlossaryName;",
        "Synonyms": "Project_Management_Risk_Evaluation;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Stakeholder_Analysis",
        "Name": "Stakeholder Analysis",
        "Status": "Approved",
        "Definition": "The process of assessing a system and potential changes to it as they relate to relevant and interested parties.",
        "Acronym": "SA",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Stakeholder_Management;Project_Management_Stakeholder_Engagement@otherGlossaryName;",
        "Synonyms": "Project_Management_Stakeholder_Assessment;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Critical_Path",
        "Name": "Critical Path",
        "Status": "Approved",
        "Definition": "The sequence of stages determining the minimum time needed for an operation.",
        "Acronym": "CP",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Project_Schedule;Project_Management_Project_Timeline@otherGlossaryName;",
        "Synonyms": "Project_Management_Critical_Sequence;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Milestone",
        "Name": "Milestone",
        "Status": "Approved",
        "Definition": "A significant point or event in a project, program, or portfolio.",
        "Acronym": "MS",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Project_Phase;Project_Management_Project_Event@otherGlossaryName;",
        "Synonyms": "Project_Management_Key_Event;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Work_Breakdown_Structure",
        "Name": "Work Breakdown Structure",
        "Status": "Approved",
        "Definition": "A hierarchical decomposition of the total scope of work to accomplish the project objectives and create the deliverables.",
        "Acronym": "WBS",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Project_Structure;Project_Management_Project_Decomposition@otherGlossaryName;",
        "Synonyms": "Project_Management_Task_Structure;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Project_Charter",
        "Name": "Project Charter",
        "Status": "Approved",
        "Definition": "A document that formally authorizes a project or a phase and provides the project manager with the authority to apply organizational resources to project activities.",
        "Acronym": "PC",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Project_Authorization;Project_Management_Project_Documentation@otherGlossaryName;",
        "Synonyms": "Project_Management_Project_Approval;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Project_Management_Project_Schedule",
        "Name": "Project Schedule",
        "Status": "Approved",
        "Definition": "A timetable that outlines the start and finish dates of project elements.",
        "Acronym": "PS",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Project_Management_Project_Timeline;Project_Management_Project_Plan@otherGlossaryName;",
        "Synonyms": "Project_Management_Project_Timetable;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    # Add more rows as needed
]

data_glossary_data = [
    {
        "Nick Name": "Data_Analytics_Big_Data",
        "Name": "Big Data",
        "Status": "Approved",
        "Definition": "Large volumes of data that can be analyzed for insights.",
        "Acronym": "BD",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Data_Warehousing;Data_Analytics_Data_Mining@otherGlossaryName;",
        "Synonyms": "Data_Analytics_Large_Data_Sets;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Data_Analytics_Data_Warehousing",
        "Name": "Data Warehousing",
        "Status": "Approved",
        "Definition": "The process of constructing and using a data warehouse.",
        "Acronym": "DW",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Big_Data;Data_Analytics_Data_Mining@otherGlossaryName;",
        "Synonyms": "Data_Analytics_Data_Storage;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Data_Analytics_Data_Mining",
        "Name": "Data Mining",
        "Status": "Approved",
        "Definition": "The practice of examining large databases in order to generate new information.",
        "Acronym": "DM",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Big_Data;Data_Analytics_Data_Warehousing@otherGlossaryName;",
        "Synonyms": "Data_Analytics_Data_Analysis;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Data_Analytics_Data_Visualization",
        "Name": "Data Visualization",
        "Status": "Approved",
        "Definition": "The graphical representation of information and data.",
        "Acronym": "DV",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Data_Analysis;Data_Analytics_Data_Presentation@otherGlossaryName;",
        "Synonyms": "Data_Analytics_Data_Graphs;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Data_Analytics_Machine_Learning",
        "Name": "Machine Learning",
        "Status": "Approved",
        "Definition": "A method of data analysis that automates analytical model building.",
        "Acronym": "ML",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Artificial_Intelligence;Data_Analytics_Deep_Learning@otherGlossaryName;",
        "Synonyms": "Data_Analytics_Automated_Learning;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Data_Analytics_Artificial_Intelligence",
        "Name": "Artificial Intelligence",
        "Status": "Approved",
        "Definition": "The simulation of human intelligence processes by machines, especially computer systems.",
        "Acronym": "AI",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Data_Analytics_Machine_Learning;Data_Analytics_Deep_Learning@otherGlossaryName;",
        "Synonyms": "Data_Analytics_AI;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    # Add more rows as needed
]

healthcare_glossary_data = [
    {
        "Nick Name": "Healthcare_Electronic_Health_Record",
        "Name": "EHR",
        "Status": "Approved",
        "Definition": "Digital version of a patient's paper chart.",
        "Acronym": "EHR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Healthcare_Health_Information_System;Healthcare_Patient_Record@otherGlossaryName;",
        "Synonyms": "Healthcare_Digital_Health_Record;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Healthcare_Health_Information_System",
        "Name": "Health Information System",
        "Status": "Approved",
        "Definition": "A system designed to manage  data.",
        "Acronym": "HIS",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Healthcare_Electronic_Health_Record;Healthcare_Patient_Record@otherGlossaryName;",
        "Synonyms": "Healthcare_HIS;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Healthcare_Patient_Record",
        "Name": "Patient Record",
        "Status": "Approved",
        "Definition": "A comprehensive record of a patient's medical history and care.",
        "Acronym": "PR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Healthcare_Electronic_Health_Record;Healthcare_Health_Information_System@otherGlossaryName;",
        "Synonyms": "Healthcare_PR;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Healthcare_Clinical_Decision_Support",
        "Name": "Clinical Decision Support",
        "Status": "Approved",
        "Definition": "A health information technology system that is designed to provide physicians and other health professionals with clinical decision support.",
        "Acronym": "CDS",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Healthcare_Electronic_Health_Record;Healthcare_Health_Information_System@otherGlossaryName;",
        "Synonyms": "Healthcare_CDS;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Healthcare_Telemedicine",
        "Name": "Telemedicine",
        "Status": "Approved",
        "Definition": "The remote diagnosis and treatment of patients by means of telecommunications technology.",
        "Acronym": "TM",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Healthcare_Telehealth;Healthcare_Remote_Consultation@otherGlossaryName;",
        "Synonyms": "Healthcare_TM;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    # Add more rows as needed
]

finance_glossary_data = [
    {
        "Nick Name": "Finance_Annual_Percentage_Rate",
        "Name": "APR",
        "Status": "Approved",
        "Definition": "The annual rate charged for borrowing or earned through an investment.",
        "Acronym": "APR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Finance_Interest_Rate;Finance_Loan_Rate@otherGlossaryName;",
        "Synonyms": "Finance_Annual_Rate;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Finance_Annual_Percentage_Rate",
        "Name": "APR",
        "Status": "Approved",
        "Definition": "The annual rate charged for borrowing or earned through an investment.",
        "Acronym": "APR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "Finance_Interest_Rate;Finance_Loan_Rate@otherGlossaryName;",
        "Synonyms": "Finance_Annual_Rate;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Finance_Compound_Interest",
        "Name": "Compound Interest",
        "Status": "Approved",
        "Definition": "Interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.",
        "Acronym": "CI",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "F",
        "Synonyms": "Finance_CI;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Finance_Debt_to_Equity_Ratio",
        "Name": "Debt to Equity Ratio",
        "Status": "Approved",
        "Definition": "A financial ratio indicating the relative proportion of shareholders' equity and debt used to  a company's assets.",
        "Acronym": "D/E",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Finance_D/E;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Finance_Return_on_Investment",
        "Name": "Return on Investment",
        "Status": "Approved",
        "Definition": "A measure used to evaluate the efficiency or profitability of an investment.",
        "Acronym": "ROI",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Finance_ROI;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    # Add more rows as needed
]

marketing_glossary_data = [
    {
        "Nick Name": "Marketing_Customer_Retention",
        "Name": "Customer Retention",
        "Status": "Approved",
        "Definition": "The ability of a company to retain its customers over a period of time.",
        "Acronym": "CR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Marketing_Client_Retention;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Marketing_Brand_Awareness",
        "Name": "Brand Awareness",
        "Status": "Approved",
        "Definition": "The extent to which consumers are familiar with the distinctive qualities or image of a particular brand of goods or services.",
        "Acronym": "BA",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Marketing_BA;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Marketing_Customer_Acquisition_Cost",
        "Name": "Customer Acquisition Cost",
        "Status": "Approved",
        "Definition": "The cost associated with convincing a consumer to buy a product/service, including research, , and advertising costs.",
        "Acronym": "CAC",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Marketing_CAC;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    {
        "Nick Name": "Marketing_Conversion_Rate",
        "Name": "Conversion Rate",
        "Status": "Approved",
        "Definition": "The percentage of visitors to a website that complete a desired goal (a conversion) out of the total number of visitors.",
        "Acronym": "CR",
        "Resources": "Microsoft Purview Project:https://web.purview.azure.com;Azure portal:https://portal.azure.com;",
        "Related Terms": "",
        "Synonyms": "Marketing_CR;",
        "Stewards": "",
        "Experts": "",
        "Parent Term Name": "",
        "IsDefinitionRichText": True,
        "Term Template Names": "System default",
    },
    # Add more rows as needed
]

# Create DataFrames for each glossary
project_glossary_df = pd.DataFrame(project_glossary_data)
data_glossary_df = pd.DataFrame(data_glossary_data)
healthcare_glossary_df = pd.DataFrame(healthcare_glossary_data)
finance_glossary_df = pd.DataFrame(finance_glossary_data)
marketing_glossary_df = pd.DataFrame(marketing_glossary_data)

# Save each DataFrame to a CSV file
project_glossary_df.to_csv("Project_Glossary.csv", index=False)
data_glossary_df.to_csv("Data_Glossary.csv", index=False)
healthcare_glossary_df.to_csv("Healthcare_Glossary.csv", index=False)
finance_glossary_df.to_csv("Finance_Glossary.csv", index=False)
marketing_glossary_df.to_csv("Marketing_Glossary.csv", index=False)

print("CSV files have been created successfully.")