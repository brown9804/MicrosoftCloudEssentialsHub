# PTUs and TPM relationship

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2024-10-01

----------

> Provisioned Throughput Units (PTUs) <br/>
> Tokens Per Minute (TPM)

| **PTUs** | **Calls per Minute** | **Tokens in Prompt** | **Tokens in Response** | **Tokens per Minute (TPM)** |
|----------|----------------------|----------------------|------------------------|-----------------------------|
| 1        | 10                   | 50                   | 100                    | 1,500                       |
| 2        | 20                   | 50                   | 100                    | 3,000                       |
| 5        | 50                   | 50                   | 100                    | 7,500                       |
| 10       | 100                  | 50                   | 100                    | 15,000                      |
| 20       | 200                  | 50                   | 100                    | 30,000                      |
| 50       | 500                  | 50                   | 100                    | 75,000                      |

> Explanation:

- **PTUs**: Provisioned Throughput Units represent the capacity of tokens that can be processed per minute.
- **Calls per Minute**: The number of API calls that can be made per minute.
- **Tokens in Prompt**: The number of tokens in the input prompt for each call.
- **Tokens in Response**: The number of tokens in the model's response for each call.
- **Tokens per Minute (TPM)**: The total number of tokens processed per minute, calculated as:

$$
\text{TPM} = \text{Calls per Minute} \times (\text{Tokens in Prompt} + \text{Tokens in Response})
$$

> Example Calculation:
For 50 PTUs:

1. **Calls per Minute**: Calculate the number of calls per minute:

$$
\text{Calls per Minute} = \text{PTUs} \times \text{Calls per PTU per Minute}
$$

$$
\text{Calls per Minute} = 50 \times 10 = 500
$$

2. **Tokens per Minute**: Calculate the total tokens per minute:

$$
\text{TPM} = \text{Calls per Minute} \times (\text{Tokens in Prompt} + \text{Tokens in Response})
$$

$$
\text{TPM} = 500 \times (50 + 100) = 500 \times 150 = 75,000
$$

This means with 50 PTUs, you can process 75,000 tokens per minute.

## Provisioned Capacity Calculator

> Improve accuracy of your estimate by adding multiple workloads to your PTU calculation. Each workload will be calculated and displayed as well as the aggregate total if both are running at the same time to your deployment.

<img width="705" alt="image" src="https://github.com/user-attachments/assets/e59c7e24-6d9b-4ea3-855c-d4f284b53e59">
