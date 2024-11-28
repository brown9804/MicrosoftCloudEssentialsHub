# Fabric Capacity Metrics + Monitoring Overview 

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-28

----------

> The `Microsoft Fabric Capacity Metrics app` is designed to provide comprehensive monitoring capabilities for Microsoft Fabric capacities. It helps administrators track capacity consumption, identify performance bottlenecks, and make informed decisions about scaling and resource allocation. The app provides detailed insights into capacity utilization, throttling, and system events, enabling proactive management of resources to ensure optimal performance.

## Wiki 

<details>
<summary><b>Table of Wiki</b> (Click to expand)</summary>

- [Install the Microsoft Fabric capacity metrics app](https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app-install?tabs=1st)
- [What is the Microsoft Fabric Capacity Metrics app?](https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app)
- [Understand the metrics app compute page](https://learn.microsoft.com/en-us/fabric/enterprise/metrics-app-compute-page)

</details>


## Microsoft Fabric Capacity Metrics app 

> This app is essential for maintaining the health and efficiency of your Microsoft Fabric capacities

| **Feature**                  | **Description**                                                                 |
|------------------------------|---------------------------------------------------------------------------------|
| **Capacity Utilization**     | Monitors the usage of Capacity Units (CUs) over time, distinguishing between interactive and background operations. |
| **Throttling**               | Displays delays and rejections based on capacity consumption, helping to manage and mitigate performance issues. |
| **System Events**            | Logs significant events such as capacity pauses and resumes, providing context for performance changes. |
| **Matrix by Item and Operation** | Breaks down metrics by individual items and operations, offering granular insights into resource usage. |

### Prerequisites
1. **Capacity Admin**: Ensure you have admin rights for the capacity you want to monitor.
2. **Power BI Pro License**: Install the app in a workspace with a Pro license to avoid throttling.

### Installation Steps

1. **Get the App**:
    - Navigate to [Microsoft Fabric](https://app.fabric.microsoft.com/). In the left panel, locate the `Apps` icon and click on `Get apps`.

        <img width="550" alt="image" src="https://github.com/user-attachments/assets/931eb614-bb29-4e03-9637-4a9ef0cc3e7a">
        
     - Search for `Microsoft Fabric Capacity Metrics`:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/a743d770-f1ea-474b-8d2c-c363e2a40e13">

     - Select `Get it now`:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/93412866-bf62-4c09-a62c-4bda280d7a40">

     - Click on `Install`:

          <img width="550" alt="image" src="https://github.com/user-attachments/assets/49aa432b-a3fd-4a2d-a504-ce08841b681e">

### Configuration Steps
1. **Run the App for the First Time**:
   - In Microsoft Fabric, go to **Apps** and select the Microsoft Fabric Capacity Metrics app.
   - When prompted with `You have to connect to your own data to view this report`, select **Connect**.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/de72c2c8-f755-41be-831d-9b756963a30b">

2. **Connect to Your Data**:
   - In the first connection window, fill in the required fields:
     - **CapacityID**: Find this in the URL of the capacity management page (e.g., `9B77CC50-E537-40E4-99B9-2B356347E584`).
          1. Navigate to the Capacity Management Page:
             - Go to the Power BI service and sign in with your admin account.
             - Click on the `Settings` gear icon in the top right corner.
             - Select `Admin Portal` from the dropdown menu.
     
                 <img width="550" alt="image" src="https://github.com/user-attachments/assets/5b3a8f2a-8062-4a2f-b121-96522088c2d7">

          2. Access Capacity Settings:
             - In the Admin Portal, go to the `Capacity settings` section.
             - Select the capacity you want to monitor.

                 <img width="550" alt="image" src="https://github.com/user-attachments/assets/64e75e78-9a33-44fc-b50a-1e041583626e">

          3. Locate the CapacityID:
             - Look at the URL in your browser’s address bar. The CapacityID is part of this URL.
             - It will look something like this: `https://app.powerbi.com/admin-portal/capacities/9B77CC50-E537-40E4-99B9-2B356347E584`.
             - The string `9B77CC50-E537-40E4-99B9-2B356347E584` is your CapacityID.

                 <img width="550" alt="image" src="https://github.com/user-attachments/assets/8b028365-bf3d-4dfd-a40e-95f355c27ff4">

     - **UTC_offset**: Enter your organization's standard time in UTC (e.g., for Central Standard Time, enter `-6`). 

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/b2f5e435-d3a0-4e2b-ae80-0376caa2e00b">

         <img width="550" alt="image" src="https://github.com/user-attachments/assets/91bffe08-d600-461f-9d44-f4b35265d662">

3. **Advanced Options** (Optional): You can disable automatic data refresh by expanding the advanced options and selecting **Off** (`On` status is recommended). Click `Next`:

     <img width="550" alt="image" src="https://github.com/user-attachments/assets/992a978c-a4af-485e-9efa-738bc261098a">

4. **Authentication and Privacy**: In the second connection window, select your **Authentication method** (default is OAuth2).

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/f1d1742b-1352-4e8f-b840-1aeafc987961">

5. **Sign In and Continue**:
   - Sign in and select a capacity from the **Capacity Name** dropdown.
   - The app may take a few minutes to load your data. If it doesn't display data immediately, refresh the app.

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/35bd1fc0-e5b3-43f0-acf8-d71310134273">

       <img width="550" alt="image" src="https://github.com/user-attachments/assets/be675f2f-82a4-4799-a72b-04cc9b47f3aa">

### Troubleshooting
- If the app doesn't show data or can't refresh, try deleting the old app and reinstalling the latest version.
- Update the semantic model credentials if needed.


