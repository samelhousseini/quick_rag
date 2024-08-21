import os
from dotenv import load_dotenv
load_dotenv()

DI_ENDPOINT = os.environ.get('DI_ENDPOINT', '')
DI_KEY = os.environ.get('DI_KEY', '')
DI_API_VERSION  = os.environ.get('DI_API_VERSION', '')

AZURE_OPENAI_RESOURCE = os.environ.get('AZURE_OPENAI_RESOURCE', '')
AZURE_OPENAI_KEY = os.environ.get('AZURE_OPENAI_KEY', "2024-02-29-preview")

AZURE_OPENAI_RESOURCE_1 = os.environ.get('AZURE_OPENAI_RESOURCE_1', '')
AZURE_OPENAI_KEY_1 = os.environ.get('AZURE_OPENAI_KEY_1', '')

AZURE_OPENAI_RESOURCE_2 = os.environ.get('AZURE_OPENAI_RESOURCE_2', '')
AZURE_OPENAI_KEY_2 = os.environ.get('AZURE_OPENAI_KEY_2', '')

AZURE_OPENAI_RESOURCE_3 = os.environ.get('AZURE_OPENAI_RESOURCE_3', '')
AZURE_OPENAI_KEY_3 = os.environ.get('AZURE_OPENAI_KEY_3', '')

AZURE_OPENAI_RESOURCE_4 = os.environ.get('AZURE_OPENAI_RESOURCE_4', '')
AZURE_OPENAI_KEY_4 = os.environ.get('AZURE_OPENAI_KEY_4', '')

AZURE_OPENAI_RESOURCE_5 = os.environ.get('AZURE_OPENAI_RESOURCE_5', '')
AZURE_OPENAI_KEY_5 = os.environ.get('AZURE_OPENAI_KEY_5', '')

AZURE_OPENAI_RESOURCE_6 = os.environ.get('AZURE_OPENAI_RESOURCE_6', '')
AZURE_OPENAI_KEY_6 = os.environ.get('AZURE_OPENAI_KEY_6', '')

AZURE_OPENAI_EMBEDDING_MODEL_RESOURCE = os.environ.get('AZURE_OPENAI_EMBEDDING_MODEL_RESOURCE', '')
AZURE_OPENAI_EMBEDDING_MODEL_RESOURCE_KEY = os.environ.get('AZURE_OPENAI_EMBEDDING_MODEL_RESOURCE_KEY', '')
AZURE_OPENAI_EMBEDDING_MODEL_API_VERSION = os.environ.get('AZURE_OPENAI_EMBEDDING_MODEL_API_VERSION', '2023-12-01-preview')


AZURE_OPENAI_MODEL = os.environ.get('AZURE_OPENAI_MODEL', '')
AZURE_OPENAI_EMBEDDING_MODEL = os.environ.get('AZURE_OPENAI_EMBEDDING_MODEL', 'text-embedding-ada-002')
AZURE_OPENAI_MODEL_VISION = os.environ.get('AZURE_OPENAI_MODEL_VISION', '')
AZURE_OPENAI_VISION_API_VERSION = os.environ.get('AZURE_OPENAI_VISION_API_VERSION', '2023-12-01-preview')

AZURE_OPENAI_API_VERSION = os.environ.get('AZURE_OPENAI_API_VERSION', '')
AZURE_OPENAI_TEMPERATURE = float(os.environ.get('AZURE_OPENAI_TEMPERATURE', '0.2'))
AZURE_OPENAI_TOP_P = os.environ.get('AZURE_OPENAI_TOP_P', '')
AZURE_OPENAI_MAX_TOKENS = os.environ.get('AZURE_OPENAI_MAX_TOKENS', '')
AZURE_OPENAI_STOP_SEQUENCE = os.environ.get('AZURE_OPENAI_STOP_SEQUENCE', '')

ROOT_PATH_INGESTION = os.environ.get('ROOT_PATH_INGESTION', '')

COG_SERV_ENDPOINT = os.environ.get('COG_SERV_ENDPOINT', '')
COG_SERV_KEY = os.environ.get('COG_SERV_KEY', '')
COG_SERV_LOCATION = os.environ.get('COG_SERV_LOCATION', '')

COG_SEARCH_ENDPOINT = os.environ.get('COG_SEARCH_ENDPOINT', '')
COG_SEARCH_ADMIN_KEY = os.environ.get('COG_SEARCH_ADMIN_KEY', '')
COG_VEC_SEARCH_API_VERSION = os.environ.get('COG_VEC_SEARCH_API_VERSION', '')

COG_SEARCH_ENDPOINT_PROD = os.environ.get('COG_SEARCH_ENDPOINT_PROD', '')
COG_SEARCH_ADMIN_KEY_PROD = os.environ.get('COG_SEARCH_ADMIN_KEY_PROD', '')

BLOB_CONN_STR = os.environ.get('BLOB_CONN_STR', '')

TRANSLATION_ENDPOINT = os.environ.get('TRANSLATION_ENDPOINT', 'https://api.cognitive.microsofttranslator.com')

SEM_INDEX_NAME = os.environ.get('SEM_INDEX_NAME', 'sc-sem')
COG_VECSEARCH_VECTOR_INDEX = os.environ.get('COG_VECSEARCH_VECTOR_INDEX', 'vec-index')

KB_INDEX_NAME = os.environ.get('KB_INDEX_NAME', 'tesla_facts_index')
KB_TOPIC = os.environ.get('KB_TOPIC', 'Tesla Model S Facts')

KB_SEM_INDEX_NAME = os.environ.get('KB_SEM_INDEX_NAME', 'sc_1')
KB_INDEXER_NAME = os.environ.get('KB_INDEXER_NAME', 'sc-indexer')
KB_DATA_SOURCE_NAME = os.environ.get('KB_DATA_SOURCE_NAME', 'sc-docs')
KB_SKILLSET_NAME = os.environ.get('KB_SKILLSET_NAME', 'sc-skills')
KB_BLOB_CONTAINER = os.environ.get('KB_BLOB_CONTAINER', 'search')
OVERLAP_TEXT = int(os.environ.get('OVERLAP_TEXT', '250'))

AZURE_VISION_ENDPOINT = os.environ.get('AZURE_VISION_ENDPOINT', '')
AZURE_VISION_KEY = os.environ.get('AZURE_VISION_KEY', '')

AZURE_OPENAI_ASSISTANTSAPI_ENDPOINT = os.environ.get('AZURE_OPENAI_ASSISTANTSAPI_ENDPOINT', '')
AZURE_OPENAI_ASSISTANTSAPI_KEY = os.environ.get('AZURE_OPENAI_ASSISTANTSAPI_KEY', '')

TEXT_CHUNK_SIZE = int(os.environ.get('TEXT_CHUNK_SIZE', '512'))
TEXT_CHUNK_OVERLAP = int(os.environ.get('TEXT_CHUNK_OVERLAP', '128'))

CHAINLIT_APP = os.environ.get('CHAINLIT_APP', '')

TENACITY_STOP_AFTER_DELAY = int(os.environ.get('TENACITY_STOP_AFTER_DELAY', '300'))
TENACITY_TIMEOUT = int(os.environ.get('TENACITY_TIMEOUT', '200'))

## AML
AML_SUBSCRIPTION_ID=os.environ.get('AML_SUBSCRIPTION_ID', '')
AML_RESOURCE_GROUP=os.environ.get('AML_RESOURCE_GROUP', '')
AML_WORKSPACE_NAME=os.environ.get('AML_WORKSPACE_NAME', '')

## Azure File Share
AZURE_FILE_SHARE_ACCOUNT=os.environ.get('AZURE_FILE_SHARE_ACCOUNT', '')
AZURE_FILE_SHARE_NAME=os.environ.get('AZURE_FILE_SHARE_NAME', '')
AZURE_FILE_SHARE_KEY=os.environ.get('AZURE_FILE_SHARE_KEY', '')

#COSMOS DB
COSMOS_URI = os.environ.get('COSMOS_URI', '')
COSMOS_KEY = os.environ.get('COSMOS_KEY', '')
COSMOS_DB_NAME = os.environ.get('COSMOS_DB_NAME', 'mmdoc')
COSMOS_CONTAINER_NAME = os.environ.get('COSMOS_CONTAINER_NAME', 'prompts')
COSMOS_CATEGORYID = os.environ.get('COSMOS_CATEGORYID', 'prompts')
COSMOS_LOG_CONTAINER = os.environ.get('COSMOS_LOG_CONTAINER', 'logs')


INITIAL_INDEX = os.environ.get('INITIAL_INDEX', 'rag-data')


BUILD_ID = os.getenv('BUILD_ID', '0.0.0')

AML_TENANT_ID = os.environ.get('AML_TENANT_ID', '')
AML_SERVICE_PRINCIPAL_ID = os.environ.get('AML_SERVICE_PRINCIPAL_ID', '')
AML_PASSWORD = os.environ.get('AML_PASSWORD', '')
AML_VMSIZE = os.environ.get('AML_VMSIZE', 'Standard_DS3_v2')
AML_CLUSTER_NAME = os.environ.get('AML_CLUSTER_NAME','mm-doc-cpu-cluster')

FULL_TEXT_TOKEN_LIMIT = int(os.environ.get('FULL_TEXT_TOKEN_LIMIT', '100000'))


AZURE_SQL_SERVER_NAME = os.environ.get('AZURE_SQL_SERVER_NAME', '')
AZURE_SQL_DATABASE_NAME = os.environ.get('AZURE_SQL_DATABASE_NAME', '')
AZURE_SQL_USERNAME = os.environ.get('AZURE_SQL_USERNAME', '')
AZURE_SQL_PASSWORD = os.environ.get('AZURE_SQL_PASSWORD', '')
AZURE_SQL_SCHEMA_NAME = os.environ.get('AZURE_SQL_SCHEMA_NAME', 'dbo')
AZURE_SQL_DRIVER = os.environ.get('AZURE_SQL_DRIVER', 'ODBC Driver 18 for SQL Server')


SEARCH_TOP_N =  int(os.environ.get('SEARCH_TOP_N', '4'))


AZURE_NEO4J_URI = os.environ.get('AZURE_NEO4J_URI', '')
AZURE_NEO4J_USERNAME = os.environ.get('AZURE_NEO4J_USERNAME', '')
AZURE_NEO4J_PASSWORD = os.environ.get('AZURE_NEO4J_PASSWORD', '')
AZURE_NEO4J_DATABASE = os.environ.get('AZURE_NEO4J_DATABASE', '')

APPLICATIONINSIGHTS_CONNECTION_STRING = os.environ.get('APPLICATIONINSIGHTS_CONNECTION_STRING', '')


# GraphRAG
USE_GRAPHRAG_OR_RAG = os.environ.get('USE_GRAPHRAG_OR_RAG', 'NO')

BICEP_GEN_FOLDER = os.environ.get('BICEP_GEN_FOLDER', 'generated_bicep')
BICEP_CORRECTION_RETRIES = int(os.environ.get('BICEP_CORRECTION_RETRIES', '5'))



# Subscription and Resource Group for ARM Validator
ARM_SUBSCRIPTION_ID = os.environ.get('ARM_SUBSCRIPTION_ID', '')
ARM_RESOURCE_GROUP_NAME = os.environ.get('ARM_RESOURCE_GROUP_NAME', '')
ARM_DEPLOYMENT_NAME = os.environ.get('ARM_DEPLOYMENT_NAME', '')