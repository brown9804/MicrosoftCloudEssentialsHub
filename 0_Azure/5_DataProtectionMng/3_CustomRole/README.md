# Custom Roles - RBAC ( Role-Based Access Control)

Costa Rica

[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-11-28

----------

> Custom roles in Azure are a powerful feature of Azure Role-Based Access Control (RBAC) that allow you to create roles tailored to the specific needs of your organization

> E.g., Imagine you have a team of developers who need to manage virtual machines but should not have access to billing information. You can create a custom role that includes permissions to start, stop, and restart virtual machines but excludes any billing-related actions.


## Wiki 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>

- [Install Azure CLI on Windows](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)
- [Tutorial: Create an Azure custom role using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-cli)
- [Tutorial: Create an Azure custom role using Azure PowerShell](https://learn.microsoft.com/en-us/azure/role-based-access-control/tutorial-custom-role-powershell)

</details>


## Overview 

> Custom roles are user-defined roles that provide fine-grained access management to Azure resources. Unlike built-in roles, which come predefined with a set of permissions, custom roles allow you to specify exactly what actions can be performed and on which resources. <br/>


| **Component**       | **Description**                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------|
| **Name**            | A unique name for the custom role.                                                                    |
| **Description**     | A brief description of what the role does.                                                            |
| **Actions**         | The specific operations that the role allows. For example, `Microsoft.Compute/virtualMachines/start/action` allows starting virtual machines. |
| **NotActions**      | Operations that are explicitly denied, even if they fall under a broader action.                      |
| **DataActions**     | Operations on data within a resource, such as reading or writing to a storage account.                |
| **NotDataActions**  | Data operations that are explicitly denied.                                                           |
| **AssignableScopes**| The scopes (e.g., subscriptions, resource groups) where the role can be assigned.                     |

Custom roles are used to:
- `Tailor Permissions`: Provide only the necessary permissions to users, reducing the risk of unauthorized access.
- `Enhance Security`: By limiting permissions to the minimum required, you enhance the security of your Azure environment.
- `Improve Compliance`: Ensure that users have permissions that align with organizational policies and compliance requirements.

  
## How to Setup

Custom roles can be created using various methods:

| **Method**         | **Description**                                                                                       |
|--------------------|-------------------------------------------------------------------------------------------------------|
| **Azure Portal**   | A user-friendly interface to define and manage custom roles.                                          |
| **Azure CLI**      | Command-line interface for scripting and automation.                                                  |
| **Azure PowerShell**| Another scripting tool for creating and managing roles.                                               |
| **REST API**       | For programmatic access and integration with other systems.                                           |


> [!IMPORTANT]
> Please ensure you log in to the admin account, as you need admin permissions to set up the custom role.

1. Sign in to Azure CLI: `az login`

<img width="550" alt="image" src="https://github.com/user-attachments/assets/83ec82fe-dea2-494e-8937-69f0cdf281b3">

- Click on `Enter`, the `highlighted` configuration is the one assigned to the account.

    <img width="550" alt="image" src="https://github.com/user-attachments/assets/fe64a968-8e5b-4bec-ad1c-0ee8f29cb38e">

2. Create a file. E.g., named `custom_role.json` with the required structure. Below is an example of a custom role for subscription access. Click [here to see the example file](./src/custom_role.json)

     ```json
        {
          "Name": "{YOUR_CUSTOM_ROLE}",
          "Description": "",
          "AssignableScopes": [
              "/subscriptions/{your-subscription-id}"
          ],
          "Actions": [
              "*",
              "Microsoft.Authorization/roleAssignments/write",
              "Microsoft.Resources/deployments/read",
              "Microsoft.Resources/deployments/write",
              "Microsoft.Resources/deployments/delete",
              "Microsoft.Resources/deployments/cancel/action",
              "Microsoft.Resources/deployments/validate/action",
              "Microsoft.Resources/deployments/whatIf/action",
              "Microsoft.Resources/deployments/exportTemplate/action"
          ],
          "NotActions": [
              "Microsoft.Authorization/*/Delete",
              "Microsoft.Authorization/elevateAccess/Action",
              "Microsoft.Blueprint/blueprintAssignments/write",
              "Microsoft.Blueprint/blueprintAssignments/delete",
              "Microsoft.Compute/galleries/share/action",
              "Microsoft.Purview/consents/write",
              "Microsoft.Purview/consents/delete",
              "Microsoft.Authorization/classicAdministrators/write",
              "Microsoft.Authorization/classicAdministrators/delete",
              "Microsoft.Authorization/denyAssignments/write",
              "Microsoft.Authorization/denyAssignments/delete",
              "Microsoft.Authorization/diagnosticSettings/write",
              "Microsoft.Authorization/diagnosticSettings/delete",
              "Microsoft.Authorization/locks/write",
              "Microsoft.Authorization/locks/delete",
              "Microsoft.Authorization/policyAssignments/delete",
              "Microsoft.Authorization/policyAssignments/write",
              "Microsoft.Authorization/policyAssignments/exempt/action",
              "Microsoft.Authorization/policyAssignments/privateLinkAssociations/write",
              "Microsoft.Authorization/policyAssignments/privateLinkAssociations/delete",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/write",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/delete",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/privateEndpointConnections/write",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/privateEndpointConnections/delete",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/privateEndpointConnectionProxies/write",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/privateEndpointConnectionProxies/delete",
              "Microsoft.Authorization/policyAssignments/resourceManagementPrivateLinks/privateEndpointConnectionProxies/validate/action",
              "Microsoft.Authorization/policyDefinitions/write",
              "Microsoft.Authorization/policyDefinitions/delete",
              "Microsoft.Authorization/policyExemptions/write",
              "Microsoft.Authorization/policyExemptions/delete",
              "Microsoft.Authorization/policySetDefinitions/write",
              "Microsoft.Authorization/policySetDefinitions/delete",
              "Microsoft.Authorization/roleAssignments/delete",
              "Microsoft.Authorization/roleAssignmentScheduleRequests/write",
              "Microsoft.Authorization/roleAssignmentScheduleRequests/cancel/action",
              "Microsoft.Authorization/roleDefinitions/write",
              "Microsoft.Authorization/roleDefinitions/delete",
              "Microsoft.Authorization/roleEligibilityScheduleRequests/write",
              "Microsoft.Authorization/roleEligibilityScheduleRequests/cancel/action",
              "Microsoft.Authorization/roleManagementPolicies/write"
          ],
          "DataActions": []
      }
  
     ```

3. Create the custom role: Use the following command to create the role using the JSON file.

```powershell
 az role definition create --role-definition {file-name}.json
```

In this example:

```powershell
az role definition create --role-definition custom_role.json
```

<img width="550" alt="image" src="https://github.com/user-attachments/assets/c4a3a705-b363-41cb-ac30-71a5c2ad7135">

4. Verify the custom role: List your custom roles to ensure it was created successfully.

```powershell
az role definition list --custom-role-only true
```

<img width="550" alt="image" src="https://github.com/user-attachments/assets/5449b403-4d1b-4bdb-9ff9-c1bfd406c6d0">

5. Validate the creation of your role. Depending on the assigned actions, you will see the role under either the pricegeled tab or the job function tab. Click on `view` to see detailed information about the actions included in the role.

  <img width="550" alt="image" src="https://github.com/user-attachments/assets/cb8672c3-668d-4118-a703-91ce9886149b">

6. Assign the custom role to the necessary users. Navigate to `Access control (IAM)`, click on `+ Add`, and select `Add role assignment`:

  <img width="600" alt="image" src="https://github.com/user-attachments/assets/3da6fd4a-f968-45ad-b285-dc834846cc0a">

- Search for the role name in either the `Job Function Roles` or `Privileged Administrator Roles` tabs. Select the role, click on `+ Select members`, add the required members, and finally click on `Review + assign`:
  
    <img width="550" alt="image" src="https://github.com/user-attachments/assets/10a5b8d3-8ff0-49eb-aaa6-a3271e1baa0c">