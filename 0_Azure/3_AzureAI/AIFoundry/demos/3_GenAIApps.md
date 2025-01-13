# AI Foundry: Develop generative AI apps - Overview 

Costa Rica

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

Last updated: 2025-01-13

------------------------------------------


## Wiki 

<details>
<summary><b>Table of Wiki Contents</b> (Click to expand)</summary>

- [Microsoft Azure AI Fundamentals: AI Overview](https://learn.microsoft.com/en-us/training/paths/get-started-with-artificial-intelligence-on-azure/)
- [Develop generative AI apps in Azure AI Foundry portal](https://learn.microsoft.com/en-us/training/paths/create-custom-copilots-ai-studio/)
- [The Azure AI Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/sdk-overview?tabs=sync&pivots=programming-language-python)
- [NLP Transformers paper](https://arxiv.org/abs/1706.03762)
- [Model summary table and region availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#model-summary-table-and-region-availability)

</details>

## Content 

<details>
<summary><b>Table of Contents</b> (Click to expand)</summary>


</details>

## Overview 

<details>
<summary><strong>Artificial Intelligence (AI)</strong></summary>
<ul>
    <li>Definition: The simulation of human intelligence in machines that are programmed to think and learn.</li>
    <li>Key Components:
        <ul>
            <li>Machine Learning (ML)</li>
            <li>Natural Language Processing (NLP)</li>
            <li>Computer Vision (CV)</li>
            <li>Robotics</li>
            <li>Expert Systems</li>
        </ul>
    </li>
    <li>
        <details>
        <summary><strong>Machine Learning (ML)</strong></summary>
        <ul>
            <li>Definition: A subset of AI that involves the use of algorithms and statistical models to enable machines to improve their performance on a task through experience.</li>
            <li>Key Components:
                <ul>
                    <li>Supervised Learning</li>
                    <li>Unsupervised Learning</li>
                    <li>Reinforcement Learning (RL)</li>
                </ul>
            </li>
            <li>
                <details>
                <summary><strong>Supervised Learning</strong></summary>
                <ul>
                    <li>Definition: A type of ML where the model is trained on labeled data.</li>
                    <li>Examples: Regression, Classification</li>
                    <li>Applications:
                        <ul>
                            <li>Spam Detection</li>
                            <li>Image Classification</li>
                            <li>Medical Diagnosis</li>
                        </ul>
                    </li>
                </ul>
                </details>
            </li>
            <li>
                <details>
                <summary><strong>Unsupervised Learning</strong></summary>
                <ul>
                    <li>Definition: A type of ML where the model is trained on unlabeled data.</li>
                    <li>Examples: Clustering, Dimensionality Reduction</li>
                    <li>Applications:
                        <ul>
                            <li>Customer Segmentation</li>
                            <li>Anomaly Detection</li>
                            <li>Market Basket Analysis</li>
                        </ul>
                    </li>
                </ul>
                </details>
            </li>
            <li>
                <details>
                <summary><strong>Reinforcement Learning (RL)</strong></summary>
                <ul>
                    <li>Definition: A type of ML where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward.</li>
                    <li>Examples: Q-Learning, Deep Q-Networks (DQN)</li>
                    <li>Applications:
                        <ul>
                            <li>Robotics</li>
                            <li>Game Playing</li>
                            <li>Recommendation Systems</li>
                        </ul>
                    </li>
                </ul>
                </details>
            </li>
        </ul>
        </details>
    </li>
    <li>
        <details>
        <summary><strong>Deep Learning (DL)</strong></summary>
        <ul>
            <li>Definition: A subset of ML that involves neural networks with many layers (deep neural networks) to model complex patterns in data.</li>
            <li>Examples: Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs)</li>
            <li>Applications:
                <ul>
                    <li>Image Recognition</li>
                    <li>Natural Language Processing</li>
                    <li>Speech Recognition</li>
                    <li>Autonomous Vehicles</li>
                </ul>
            </li>
        </ul>
        </details>
    </li>
</ul>
</details>

<details>
<summary><strong>Natural Language Processing (NLP)</strong></summary>
<ul>
    <li>Definition: A field of AI focused on the interaction between computers and human language.</li>
    <li>Key Components:
        <ul>
            <li>Text Preprocessing: Tokenization, stemming, lemmatization, and stop words removal.</li>
            <li>Part-of-Speech Tagging: Identifying grammatical parts of speech.</li>
            <li>Named Entity Recognition (NER): Extracting entities like names, dates, and locations.</li>
            <li>Sentiment Analysis: Determining the emotional tone of text.</li>
            <li>Machine Translation: Translating text between languages.</li>
            <li>Topic Modeling: Identifying main themes within text.</li>
        </ul>
    </li>
    <li>
        <details>
        <summary><strong>Large Language Models (LLMs)</strong></summary>
        <ul>
            <li>Definition: Large-scale neural networks trained on vast amounts of text data to generate human-like text.</li>
            <li>Key Features:
                <ul>
                    <li>Pre-training and Fine-tuning: Training on large corpora and then fine-tuning for specific tasks.</li>
                    <li>Transformer Architecture: Handling sequential data and capturing long-range dependencies.</li>
                    <li>Contextual Understanding: Generating text based on context.</li>
                    <li>High Scalability</li>
                </ul>
            </li>
            <li>Applications:
                <ul>
                    <li>Text Generation</li>
                    <li>Question Answering</li>
                    <li>Conversational Agents</li>
                    <li>Content Creation</li>
                    <li>Code Generation</li>
                </ul>
            </li>
        </ul>
        </details>
    </li>
    <li>
        <details>
        <summary><strong>Retrieval-Augmented Generation (RAG)</strong></summary>
        <ul>
            <li>Definition: Enhances language models by retrieving external knowledge in real-time. This allows the model to access up-to-date information while generating responses.</li>
            <li>Key Features:
                <ul>
                    <li>Real-time Data Retrieval</li>
                    <li>Dynamic Knowledge Access</li>
                    <li>Flexible and Up-to-date Responses</li>
                    <li>Integration with External Databases or APIs</li>
                </ul>
            </li>
            <li>Applications:
                <ul>
                    <li>Real-time Information Retrieval</li>
                    <li>Dynamic Content Generation</li>
                    <li>Complex Query Handling</li>
                    <li>Customer Support</li>
                </ul>
            </li>
        </ul>
        </details>
    </li>
    <li>
        <details>
        <summary><strong>Cache-Augmented Generation (CAG)</strong></summary>
        <ul>
            <li>Definition: Uses preloaded knowledge stored within the model for faster and more precise responses. This approach is ideal for scenarios where the information is stable and doesn't change frequently.</li>
            <li>Key Features:
                <ul>
                    <li>Preloaded Knowledge</li>
                    <li>Precomputed Memory (Key-Value Cache)</li>
                    <li>Fast and Error-free Responses</li>
                    <li>Efficient Context Management</li>
                </ul>
            </li>
            <li>Applications:
                <ul>
                    <li>Static Knowledge Retrieval</li>
                    <li>Efficient Response Generation</li>
                    <li>Scenarios with Stable Information</li>
                    <li>Offline Applications</li>
                </ul>
            </li>
        </ul>
        </details>
    </li>
</ul>
</details>

<details>
<summary><strong>Computer Vision (CV)</strong></summary>
<ul>
    <li>Definition: A field of AI that enables computers to interpret and make decisions based on visual data. It involves techniques for processing and analyzing images and videos.</li>
    <li>Key Features:
        <ul>
            <li>Image Recognition</li>
            <li>Object Detection</li>
            <li>Image Segmentation</li>
            <li>Facial Recognition</li>
            <li>Optical Character Recognition (OCR)</li>
        </ul>
    </li>
    <li>Applications:
        <ul>
            <li>Autonomous Vehicles</li>
            <li>Medical Imaging</li>
            <li>Surveillance</li>
            <li>Augmented Reality</li>
            <li>Image and Video Analysis</li>
        </ul>
    </li>
</ul>
</details>

<details>
<summary><strong>Reinforcement Learning (RL)</strong></summary>
<ul>
    <li>Definition: A type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward. The agent learns through trial and error, receiving feedback from its actions.</li>
    <li>Key Features:
        <ul>
            <li>Trial and Error Learning</li>
            <li>Reward-based Feedback</li>
            <li>Policy Optimization</li>
            <li>Exploration and Exploitation</li>
        </ul>
    </li>
    <li>Applications:
        <ul>
            <li>Robotics</li>
            <li>Game Playing</li>
            <li>Recommendation Systems</li>
            <li>Autonomous Systems</li>
            <li>Financial Trading</li>
        </ul>
    </li>
</ul>
</details>

<details>
<summary><strong>Generative Adversarial Network (GAN)</strong></summary>
<ul>
    <li>Definition: A class of machine learning frameworks where two neural networks contest with each other to generate new, synthetic data. One network generates data (generator) while the other evaluates it (discriminator).</li>
    <li>Key Features:
        <ul>
            <li>Generator and Discriminator Networks</li>
            <li>Adversarial Training</li>
            <li>Realistic Data Generation</li>
            <li>Data Augmentation</li>
        </ul>
    </li>
    <li>Applications:
        <ul>
            <li>Image Synthesis</li>
            <li>Data Augmentation</li>
            <li>Style Transfer</li>
            <li>Deepfake Creation</li>
            <li>Art Generation</li>
        </ul>
    </li>
</ul>
</details>

| **Acronym** | **Full Name** | **Category** | **Description** | **Key Features** | **Applications** |
|-------------|----------------|--------------|-----------------|------------------|------------------|
| **NLP**     | Natural Language Processing | AI Field | A field of AI focused on the interaction between computers and human language. It involves enabling computers to understand, interpret, and generate human language in a meaningful way. | - Text preprocessing (tokenization, stemming, lemmatization, stop words removal)<br/>- Part-of-speech tagging<br/>- Named entity recognition (NER)<br/>- Sentiment analysis<br/>- Machine translation<br/>- Topic modeling | - Chatbots<br/>- Sentiment analysis<br/>- Language translation<br/>- Text summarization<br/>- Information retrieval |
| **CV**      | Computer Vision | AI Field | A field of AI that enables computers to interpret and make decisions based on visual data. It involves techniques for processing and analyzing images and videos. | - Image recognition<br/>- Object detection<br/>- Image segmentation<br/>- Facial recognition<br/>- Optical character recognition (OCR) | - Autonomous vehicles<br/>- Medical imaging<br/>- Surveillance<br/>- Augmented reality<br/>- Image and video analysis |
| **RL**      | Reinforcement Learning | AI Field | A type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward. The agent learns through trial and error, receiving feedback from its actions. | - Trial and error learning<br/>- Reward-based feedback<br/>- Policy optimization<br/>- Exploration and exploitation | - Robotics<br/>- Game playing<br/>- Recommendation systems<br/>- Autonomous systems<br/>- Financial trading |
| **LLM**     | Large Language Model | Model | Large-scale neural networks trained on vast amounts of text data to generate human-like text. These models can perform a wide range of language tasks, from answering questions to writing essays. | - Pre-training and fine-tuning<br/>- Transformer architecture<br/>- Contextual understanding<br/>- High scalability | - Text generation<br/>- Question answering<br/>- Conversational agents<br/>- Content creation<br/>- Code generation |
| **GAN**     | Generative Adversarial Network | Model | A class of machine learning frameworks where two neural networks contest with each other to generate new, synthetic data. One network generates data (generator) while the other evaluates it (discriminator). | - Generator and discriminator networks<br/>- Adversarial training<br/>- Realistic data generation<br/>- Data augmentation | - Image synthesis<br/>- Data augmentation<br/>- Style transfer<br/>- Deepfake creation<br/>- Art generation |
| **RAG**     | Retrieval-Augmented Generation | Technique | Enhances language models by retrieving external knowledge in real-time. This allows the model to access up-to-date information while generating responses. | - Real-time data retrieval<br/>- Dynamic knowledge access<br/>- Flexible and up-to-date responses<br/>- Integration with external databases or APIs | - Real-time information retrieval<br/>- Dynamic content generation<br/>- Complex query handling<br/>- Customer support |
| **CAG**     | Cache-Augmented Generation | Technique | Uses preloaded knowledge stored within the model for faster and more precise responses. This approach is ideal for scenarios where the information is stable and doesn't change frequently. | - Preloaded knowledge<br/>- Precomputed memory (key-value cache)<br/>- Fast and error-free responses<br/>- Efficient context management | - Static knowledge retrieval<br/>- Efficient response generation<br/>- Scenarios with stable information<br/>- Offline applications |


## Deploy a language model with Azure AI Foundry

| **Activity**        | **Azure OpenAI models**                                                             | **Models deployed as Serverless APIs (pay-as-you-go)**                          | **Models deployed with user-managed compute**                                  |
|---------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Deploy the model**| No, you aren’t billed for deploying an Azure OpenAI model to your project.          | Yes, you’re billed minimally per the infrastructure of the endpoint.            | Yes, you’re billed for the infrastructure hosting the model per minute.        |
| **Call the endpoint**| Yes, you’re billed based on your token usage.                                       | Yes, you’re billed based on your token usage.                                   | None.                                                                          |
| **Setup Complexity**| Low - Managed by Azure, minimal setup required.                                      | Medium - Requires setting up serverless functions and endpoints.                | High - Requires setting up and managing infrastructure.                        |
| **Scalability**     | High - Automatically scales with demand.                                            | Medium - Scales with serverless infrastructure, but may have limits.            | High - Can be scaled based on infrastructure capacity.                         |
| **Maintenance**     | Low - Managed by Azure, minimal maintenance required.                               | Medium - Requires monitoring and maintaining serverless functions.              | High - Requires ongoing maintenance of infrastructure and updates.             |
| **Cost Efficiency** | Variable - Costs based on token usage, can be cost-effective for low to moderate usage. | Variable - Costs based on token usage and infrastructure, can be cost-effective for moderate usage. | Variable - Costs based on infrastructure usage, can be cost-effective for high usage. |
| **Flexibility**     | Medium - Limited to Azure OpenAI models and configurations.                         | High - Can deploy custom models and configurations.                             | High - Full control over model deployment and configurations.                  |
| **Security**        | High - Managed by Azure with built-in security features.                            | Medium - Security depends on serverless infrastructure and configurations.      | High - Full control over security configurations and compliance.               |
| **Performance**     | High - Optimized by Azure for performance and reliability.                          | Medium - Performance depends on serverless infrastructure and configurations.   | High - Performance can be optimized based on infrastructure specifications.    |
| **Integration**     | High - Seamless integration with other Azure services.                              | Medium - Can integrate with other services, but may require additional setup.   | High - Full control over integration with other services and systems.          |
| **Customization**   | Low - Limited customization options.                                                | High - Can customize models and endpoints as needed.                            | High - Full customization of models, infrastructure, and endpoints.            |
| **Support**         | High - Azure provides extensive support and documentation.                          | Medium - Support depends on the serverless platform and configurations.         | High - Full control over support and troubleshooting.                          |

<div align="center">
  <h3 style="color: #4CAF50;">Total Visitors</h3>
  <img src="https://profile-counter.glitch.me/brown9804/count.svg" alt="Visitor Count" style="border: 2px solid #4CAF50; border-radius: 5px; padding: 5px;"/>
</div>
