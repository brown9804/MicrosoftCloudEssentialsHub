# Azure OpenAI: Models Deployment Overview 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-08-01

----------

## How to 
1. Create an Azure OpenAI Resource
    - Sign in to the [Azure portal](https://portal.azure.com).
    - Navigate to **Create a resource** and search for **Azure OpenAI**.
    - Follow the prompts to create your resource, ensuring it's in a region that supports the models you need.

      <img width="500" alt="image" src="https://github.com/user-attachments/assets/7719500c-9f47-4afe-983e-19fa3027138e">
      
> [!NOTE]
> When creating your Azure OpenAI resource, ensure you select a resource group and region that supports the specific model versions you want to use. This can affect latency and availability.

2. Deploy the Model
    - Once your resource is created, go to the **Azure OpenAI Studio**.
    - Select **Deployments** and click on **Create**.
    - Choose the model version you want to deploy (e.g., `gpt-4o-mini-2024-07-18`).

      <img width="500" alt="image" src="https://github.com/user-attachments/assets/e4f11fff-7ab2-4bb5-bfbb-eaab13d88932">

> [!NOTE]  
> After deploying the model, you'll receive an API key. Keep this key secure and manage it through Azure's Key Vault for added security. <br/>
> Be aware of the usage quotas and pricing associated with each model. You can monitor your usage and set up alerts in the Azure portal to avoid unexpected costs.

3. Configure the Model
    - **Fine-tuning (Optional)**: If you need to fine-tune the model, you can do so by preparing your training data and following the fine-tuning workflow in the Azure OpenAI Studio.
    - **Structured Outputs**: For the GPT-4o-2024-08-06 model, you can specify JSON Schemas within your API calls to ensure the AI output adheres to your defined structure.

> [!NOTE]
> **Temperature and Max Tokens**: Adjust the `temperature` parameter to control the randomness of the output and `max_tokens` to limit the length of the response. <br/>
> **Top-p and Frequency Penalty**: Use `top_p` to control the diversity of the output and `frequency_penalty` to reduce repetitive responses.

4. Integration and Testing
    - Integrate the deployed model into your application using the provided API endpoints.
    - Test thoroughly to ensure the model meets your requirements and adheres to any specified output formats.

> [!NOTE]
> Implement robust error handling in your application to manage API rate limits, timeouts, and other potential issues.
> Use logging to track API calls and responses for debugging and performance monitoring.

## Example API Call

Here's a basic example of how you might call the model using Python:

```python
import openai

openai.api_key = "YOUR_API_KEY"

response = openai.Completion.create(
  model="gpt-4o-2024-08-06",
  prompt="Your prompt here",
  max_tokens=100
)

print(response.choices[0].text)
```
