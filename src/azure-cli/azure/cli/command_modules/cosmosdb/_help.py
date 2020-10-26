# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['cosmosdb'] = """
type: group
short-summary: Manage Azure Cosmos DB database accounts.
"""

helps['cosmosdb cassandra'] = """
type: group
short-summary: Manage Cassandra resources of Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace'] = """
type: group
short-summary: Manage Azure Cosmos DB Cassandra keyspaces.
"""

helps['cosmosdb cassandra keyspace create'] = """
type: command
short-summary: Create an Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace delete'] = """
type: command
short-summary: Delete the Cassandra keyspace under an Azure Cosmos DB account.
examples:
  - name: Delete the Cassandra keyspace under an Azure Cosmos DB account. (autogenerated)
    text: az cosmosdb cassandra keyspace delete --account-name MyAccount --name MyKeyspace --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb cassandra keyspace list'] = """
type: command
short-summary: List the Cassandra keyspaces under an Azure Cosmos DB account.
examples:
  - name: List the Cassandra keyspaces under an Azure Cosmos DB account. (autogenerated)
    text: az cosmosdb cassandra keyspace list --account-name MyAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb cassandra keyspace show'] = """
type: command
short-summary: Show the details of a Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput'] = """
type: group
short-summary: Manage throughput of Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput show'] = """
type: command
short-summary: Get the throughput of the Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput update'] = """
type: command
short-summary: Update the throughput of the Cassandra keyspace under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra keyspace throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the Cassandra keyspace between autoscale and manually provisioned.
"""

helps['cosmosdb cassandra table'] = """
type: group
short-summary: Manage Azure Cosmos DB Cassandra tables.
"""

helps['cosmosdb cassandra table create'] = """
type: command
short-summary: Create an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: Create an Azure Cosmos DB Cassandra table.
    text: az cosmosdb cassandra table create -g MyResourceGroup -a MyAccount -k MyKeyspace -n MyTable --schema @indexes-file.json --throughput "500" --ttl 1000
    crafted: true
"""

helps['cosmosdb cassandra table delete'] = """
type: command
short-summary: Delete the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table list'] = """
type: command
short-summary: List the Cassandra tables under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: List the Cassandra tables under an Azure Cosmos DB Cassandra keyspace. (autogenerated)
    text: az cosmosdb cassandra table list --account-name MyAccount --keyspace-name MyKeyspace --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb cassandra table show'] = """
type: command
short-summary: Show the details of a Cassandra table under an Azure Cosmos DB Cassandra keyspace.
"""

helps['cosmosdb cassandra table throughput'] = """
type: group
short-summary: Manage throughput of Cassandra table under an Azure Cosmos DB account.
"""

helps['cosmosdb cassandra table throughput show'] = """
type: command
short-summary: Get the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: Get the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace. (autogenerated)
    text: az cosmosdb cassandra table throughput show --account-name MyAccount --keyspace-name MyKeyspace --name MyTable --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb cassandra table throughput update'] = """
type: command
short-summary: Update the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: Update the throughput of the Cassandra table under an Azure Cosmos DB Cassandra keyspace. (autogenerated)
    text: |
        az cosmosdb cassandra table throughput update --account-name MyAccount --keyspace-name MyKeyspace --name MyTable --resource-group MyResourceGroup --throughput "500"
    crafted: true
"""

helps['cosmosdb cassandra table throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the Cassandra table between autoscale and manually provisioned.
"""

helps['cosmosdb cassandra table update'] = """
type: command
short-summary: Update an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
examples:
  - name: Update an Cassandra table under an Azure Cosmos DB Cassandra keyspace. (autogenerated)
    text: az cosmosdb cassandra table update --account-name MyAccount --keyspace-name MyKeyspace --name MyTable --resource-group MyResourceGroup --schema @indexes-file.json
    crafted: true
"""

helps['cosmosdb check-name-exists'] = """
type: command
short-summary: Checks if an Azure Cosmos DB account name exists.
examples:
  - name: Checks if an Azure Cosmos DB account name exists. (autogenerated)
    text: az cosmosdb check-name-exists --name MyCosmosDBDatabaseAccount
    crafted: true
"""

helps['cosmosdb collection'] = """
type: group
short-summary: Manage Azure Cosmos DB collections.
"""

helps['cosmosdb create'] = """
type: command
short-summary: Creates a new Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Creates a new Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb create -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""

helps['cosmosdb database'] = """
type: group
short-summary: Manage Azure Cosmos DB databases.
"""

helps['cosmosdb database create'] = """
type: command
short-summary: Creates an Azure Cosmos DB database
examples:
  - name: Creates an Azure Cosmos DB database.
    text: az cosmosdb database create --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --db-name MyDatabase
    crafted: true
"""

helps['cosmosdb database delete'] = """
type: command
short-summary: Deletes an Azure Cosmos DB database
examples:
  - name: Deletes an Azure Cosmos DB database (autogenerated)
    text: az cosmosdb database delete --db-name MyDatabase --name MyCosmosDBDatabaseAccount --resource-group-name MyResourceGroup
    crafted: true
"""

helps['cosmosdb database exists'] = """
type: command
short-summary: Returns a boolean indicating whether the database exists
examples:
  - name: Returns a boolean indicating whether the database exists (autogenerated)
    text: az cosmosdb database exists --db-name MyDatabase --name MyCosmosDBDatabaseAccount --resource-group-name MyResourceGroup
    crafted: true
"""

helps['cosmosdb database list'] = """
type: command
short-summary: Lists all Azure Cosmos DB databases
examples:
  - name: Lists all Azure Cosmos DB databases (autogenerated)
    text: az cosmosdb database list --name MyCosmosDBDatabaseAccount --resource-group-name MyResourceGroup
    crafted: true
"""

helps['cosmosdb database show'] = """
type: command
short-summary: Shows an Azure Cosmos DB database
examples:
  - name: Shows an Azure Cosmos DB database (autogenerated)
    text: az cosmosdb database show --db-name MyDatabase --name MyCosmosDBDatabaseAccount --resource-group-name MyResourceGroup
    crafted: true
"""

helps['cosmosdb delete'] = """
type: command
short-summary: Deletes an Azure Cosmos DB database account.
examples:
  - name: Deletes an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb delete --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb failover-priority-change'] = """
type: command
short-summary: Changes the failover priority for the Azure Cosmos DB database account.
examples:
  - name: Changes the failover priority for the Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb failover-priority-change --failover-policies regionName=failoverPriority --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb gremlin'] = """
type: group
short-summary: Manage Gremlin resources of Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database'] = """
type: group
short-summary: Manage Azure Cosmos DB Gremlin databases.
"""

helps['cosmosdb gremlin database create'] = """
type: command
short-summary: Create an Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database delete'] = """
type: command
short-summary: Delete the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database list'] = """
type: command
short-summary: List the Gremlin databases under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database show'] = """
type: command
short-summary: Show the details of a Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput'] = """
type: group
short-summary: Manage throughput of Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput show'] = """
type: command
short-summary: Get the throughput of the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput update'] = """
type: command
short-summary: Update the throughput of the Gremlin database under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin database throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the Gremlin database between autoscale and manually provisioned.
"""

helps['cosmosdb gremlin graph'] = """
type: group
short-summary: Manage Azure Cosmos DB Gremlin graphs.
"""

helps['cosmosdb gremlin graph create'] = """
type: command
short-summary: Create an Gremlin graph under an Azure Cosmos DB Gremlin database.
examples:
  - name: Create an Azure Cosmos DB Gremlin graph.
    text: az cosmosdb gremlin graph create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyGraph --partition-key-path "/my/path" --idx @policy-file.json --ttl 1000 --throughput "700"
    crafted: true
"""

helps['cosmosdb gremlin graph delete'] = """
type: command
short-summary: Delete the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph list'] = """
type: command
short-summary: List the Gremlin graphs under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph show'] = """
type: command
short-summary: Show the details of a Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph throughput'] = """
type: group
short-summary: Manage throughput of Gremlin graph under an Azure Cosmos DB account.
"""

helps['cosmosdb gremlin graph throughput show'] = """
type: command
short-summary: Get the throughput of the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph throughput update'] = """
type: command
short-summary: Update the throughput of the Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb gremlin graph throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the Gremlin Graph between autoscale and manually provisioned.
"""

helps['cosmosdb gremlin graph update'] = """
type: command
short-summary: Update an Gremlin graph under an Azure Cosmos DB Gremlin database.
"""

helps['cosmosdb keys'] = """
type: group
short-summary: Manage Azure Cosmos DB keys.
"""

helps['cosmosdb keys list'] = """
type: command
short-summary: List the access keys or connection strings for a Azure Cosmos DB database account.
examples:
  - name: List the access keys or connection strings for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb keys list --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription --type keys
    crafted: true
"""

helps['cosmosdb list'] = """
type: command
short-summary: List Azure Cosmos DB database accounts.
"""

helps['cosmosdb list-connection-strings'] = """
type: command
short-summary: List the connection strings for a Azure Cosmos DB database account.
examples:
  - name: List the connection strings for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-connection-strings --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb list-keys'] = """
type: command
short-summary: List the access keys for a Azure Cosmos DB database account.
examples:
  - name: List the access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup --subscription MySubscription
    crafted: true
"""

helps['cosmosdb list-read-only-keys'] = """
type: command
short-summary: List the read-only access keys for a Azure Cosmos DB database account.
examples:
  - name: List the read-only access keys for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb list-read-only-keys --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb mongodb'] = """
type: group
short-summary: Manage MongoDB resources of Azure Cosmos DB account.
"""

helps['cosmosdb mongodb collection'] = """
type: group
short-summary: Manage Azure Cosmos DB MongoDB collections.
"""

helps['cosmosdb mongodb collection create'] = """
type: command
short-summary: Create an MongoDB collection under an Azure Cosmos DB MongoDB database.
examples:
  - name: Create an Azure Cosmos DB MongoDB collection.
    text: az cosmosdb mongodb collection create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyCollection --shard "ShardingKey" --idx @indexes-file.json --throughput "500"
    crafted: true
"""

helps['cosmosdb mongodb collection delete'] = """
type: command
short-summary: Delete the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection list'] = """
type: command
short-summary: List the MongoDB collections under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection show'] = """
type: command
short-summary: Show the details of a MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection throughput'] = """
type: group
short-summary: Manage throughput of MongoDB collection under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb collection throughput show'] = """
type: command
short-summary: Get the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection throughput update'] = """
type: command
short-summary: Update the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb collection throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the MongoDB collection between autoscale and manually provisioned.
"""

helps['cosmosdb mongodb collection update'] = """
type: command
short-summary: Update an MongoDB collection under an Azure Cosmos DB MongoDB database.
"""

helps['cosmosdb mongodb database'] = """
type: group
short-summary: Manage Azure Cosmos DB MongoDB databases.
"""

helps['cosmosdb mongodb database create'] = """
type: command
short-summary: Create an MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database delete'] = """
type: command
short-summary: Delete the MongoDB database under an Azure Cosmos DB account.
examples:
  - name: Delete the MongoDB database under an Azure Cosmos DB account. (autogenerated)
    text: az cosmosdb mongodb database delete --account-name MyAccount --name MyDatabase --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb mongodb database list'] = """
type: command
short-summary: List the MongoDB databases under an Azure Cosmos DB account.
examples:
  - name: List the MongoDB databases under an Azure Cosmos DB account. (autogenerated)
    text: az cosmosdb mongodb database list --account-name MyAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb mongodb database show'] = """
type: command
short-summary: Show the details of a MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput'] = """
type: group
short-summary: Manage throughput of MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput show'] = """
type: command
short-summary: Get the throughput of the MongoDB database under an Azure Cosmos DB account.
"""

helps['cosmosdb mongodb database throughput update'] = """
type: command
short-summary: Update the throughput of the MongoDB database under an Azure Cosmos DB account.
examples:
  - name: Update the throughput of the MongoDB database under an Azure Cosmos DB account. (autogenerated)
    text: |
        az cosmosdb mongodb database throughput update --account-name MyAccount --name MyDatabase --resource-group MyResourceGroup --throughput "500"
    crafted: true
"""

helps['cosmosdb mongodb database throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the MongoDB database between autoscale and manually provisioned.
"""

helps['cosmosdb network-rule'] = """
type: group
short-summary: Manage Azure Cosmos DB network rules.
"""

helps['cosmosdb private-endpoint-connection'] = """
type: group
short-summary: Manage Azure Cosmos DB private endpoint connections.
"""

helps['cosmosdb private-endpoint-connection approve'] = """
type: command
short-summary: Approve the specified private endpoint connection associated with Azure Cosmos DB.
examples:
  - name: Approve the specified private endpoint connection associated with Azure Cosmos DB.
    text: az cosmosdb private-endpoint-connection approve --account-name MyAccount --name MyPrivateEndpoint --resource-group MyResourceGroup --description "Approved"
"""

helps['cosmosdb private-endpoint-connection delete'] = """
type: command
short-summary: Delete the specified private endpoint connection associated with Azure Cosmos DB.
examples:
  - name: Delete the specified private endpoint connection associated with Azure Cosmos DB.
    text: az cosmosdb private-endpoint-connection delete --account-name MyAccount --name MyPrivateEndpoint --resource-group MyResourceGroup

"""

helps['cosmosdb private-endpoint-connection reject'] = """
type: command
short-summary: Reject the specified private endpoint connection associated with Azure Cosmos DB.
examples:
  - name: Reject the specified private endpoint connection associated with Azure Cosmos DB.
    text: az cosmosdb private-endpoint-connection reject --account-name MyAccount --name MyPrivateEndpoint --resource-group MyResourceGroup --description "Rejected"
"""

helps['cosmosdb private-endpoint-connection show'] = """
type: command
short-summary: Show details of a private endpoint connection associated with Azure Cosmos DB.
examples:
  - name: Show details of a private endpoint connection associated with Azure Cosmos DB.
    text: az cosmosdb private-endpoint-connection show --account-name MyAccount --name MyPrivateEndpoint --resource-group MyResourceGroup
"""

helps['cosmosdb private-link-resource'] = """
type: group
short-summary: Manage Azure Cosmos DB private link resources.
"""

helps['cosmosdb private-link-resource list'] = """
type: command
short-summary: List the private link resources supported for Azure Cosmos DB.
example:
  - name: List the private link resources supported for Azure Cosmos DB.
    text: cosmosdb private-link-resource list --account-name MyAccount --resource-group MyResourceGroup
"""

helps['cosmosdb regenerate-key'] = """
type: command
short-summary: Regenerate an access key for a Azure Cosmos DB database account.
examples:
  - name: Regenerate an access key for a Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb regenerate-key --key-kind primary --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb show'] = """
type: command
short-summary: Get the details of an Azure Cosmos DB database account.
examples:
  - name: Get the details of an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb show --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb sql'] = """
type: group
short-summary: Manage SQL resources of Azure Cosmos DB account.
"""

helps['cosmosdb sql stored-procedure'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL stored procedures.
"""

helps['cosmosdb sql stored-procedure create'] = """
type: command
short-summary: Create an SQL stored procedure under an Azure Cosmos DB SQL container.
examples:
  - name: Create an Azure Cosmos DB SQL stored procedure.
    text: az cosmosdb sql stored-procedure create -g MyResourceGroup -a MyAccount -d MyDatabase -c MyContainer -n MyStoredProcedure -b StoredProcedureBody
    crafted: true
"""

helps['cosmosdb sql stored-procedure delete'] = """
type: command
short-summary: Delete the SQL stored procedure under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql stored-procedure list'] = """
type: command
short-summary: List the SQL stored procedures under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql stored-procedure show'] = """
type: command
short-summary: Show the details of a SQL stored procedure under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql'] = """
type: group
short-summary: Manage SQL resources of Azure Cosmos DB account.
"""

helps['cosmosdb sql trigger'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL triggers.
"""

helps['cosmosdb sql trigger create'] = """
type: command
short-summary: Create an SQL trigger under an Azure Cosmos DB SQL container.
examples:
  - name: Create an Azure Cosmos DB SQL trigger.
    text: az cosmosdb sql trigger create -g MyResourceGroup -a MyAccount -d MyDatabase -c MyContainer -n MyTrigger -b TriggerBody
    crafted: true
"""

helps['cosmosdb sql trigger delete'] = """
type: command
short-summary: Delete the SQL trigger under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql trigger list'] = """
type: command
short-summary: List the SQL triggers under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql trigger show'] = """
type: command
short-summary: Show the details of a SQL trigger under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql user-defined-function'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL user defined functions.
"""

helps['cosmosdb sql user-defined-function create'] = """
type: command
short-summary: Create an SQL user defined function under an Azure Cosmos DB SQL container.
examples:
  - name: Create an Azure Cosmos DB SQL user defined function.
    text: az cosmosdb sql user-defined-function create -g MyResourceGroup -a MyAccount -d MyDatabase -c MyContainer -n MyUserDefinedFunction -b UserDefinedFunctionBody
    crafted: true
"""

helps['cosmosdb sql user-defined-function delete'] = """
type: command
short-summary: Delete the SQL user defined function under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql user-defined-function list'] = """
type: command
short-summary: List the SQL user defined functions under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql user-defined-function show'] = """
type: command
short-summary: Show the details of a SQL user defined function under an Azure Cosmos DB SQL container.
"""

helps['cosmosdb sql container'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL containers.
"""

helps['cosmosdb sql container create'] = """
type: command
short-summary: Create an SQL container under an Azure Cosmos DB SQL database.
examples:
  - name: Create an Azure Cosmos DB SQL container.
    text: az cosmosdb sql container create -g MyResourceGroup -a MyAccount -d MyDatabase -n MyContainer --partition-key-path "/my/path" --idx @policy-file.json --ttl 1000 --throughput "700"
    crafted: true
"""

helps['cosmosdb sql container delete'] = """
type: command
short-summary: Delete the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container list'] = """
type: command
short-summary: List the SQL containers under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container show'] = """
type: command
short-summary: Show the details of a SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container throughput'] = """
type: group
short-summary: Manage throughput of SQL container under an Azure Cosmos DB account.
"""

helps['cosmosdb sql container throughput show'] = """
type: command
short-summary: Get the throughput of the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container throughput update'] = """
type: command
short-summary: Update the throughput of the SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql container throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the SQL container between autoscale and manually provisioned.
"""

helps['cosmosdb sql container update'] = """
type: command
short-summary: Update an SQL container under an Azure Cosmos DB SQL database.
"""

helps['cosmosdb sql database'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL databases.
"""

helps['cosmosdb sql database create'] = """
type: command
short-summary: Create an SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database delete'] = """
type: command
short-summary: Delete the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database list'] = """
type: command
short-summary: List the SQL databases under an Azure Cosmos DB account.
examples:
  - name: List the SQL databases under an Azure Cosmos DB account (autogenerated)
    text: az cosmosdb sql database list --account-name MyAccount --resource-group MyResourceGroup
    crafted: true
"""

helps['cosmosdb sql database show'] = """
type: command
short-summary: Show the details of a SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput'] = """
type: group
short-summary: Manage throughput of SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput show'] = """
type: command
short-summary: Get the throughput of the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput update'] = """
type: command
short-summary: Update the throughput of the SQL database under an Azure Cosmos DB account.
"""

helps['cosmosdb sql database throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the SQL database between autoscale and manually provisioned.
"""

helps['cosmosdb sql role definition'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL role definitions.
"""

helps['cosmosdb sql role definition create'] = """
type: command
short-summary: Create a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb role definition create -a MyAccount -g MyResourceGroup -b @role-definition.json
"""

helps['cosmosdb sql role definition delete'] = """
type: command
short-summary: Delete a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb role definition delete -a MyAccount -g MyResourceGroup -i RoleDefinitionId
"""

helps['cosmosdb sql role definition exists'] = """
type: command
short-summary: Checks if an Azure Cosmos DB role definition exists.
examples:
  - name: Checks if an Azure Cosmos DB role definition exists.
    text: az cosmosdb role definition exists -a MyAccount -g MyResourceGroup -i RoleDefinitionId
"""

helps['cosmosdb sql role definition list'] = """
type: command
short-summary: List all SQL role definitions under an Azure Cosmos DB account.
examples:
  - name: List all SQL role definitions under an Azure Cosmos DB account.
    text: az cosmosdb role definition list -a MyAccount -g MyResourceGroup
"""

helps['cosmosdb sql role definition show'] = """
type: command
short-summary: Show the properties of a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Show the properties of a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb role definition show -a MyAccount -g MyResourceGroup -i RoleDefinitionId
"""

helps['cosmosdb sql role definition update'] = """
type: command
short-summary: Update a SQL role definition under an Azure Cosmos DB account.
examples:
  - name: Update a SQL role definition under an Azure Cosmos DB account.
    text: az cosmosdb role definition update -a MyAccount -g MyResourceGroup -b @role-definition.json
"""

helps['cosmosdb sql role assignment'] = """
type: group
short-summary: Manage Azure Cosmos DB SQL role assignments.
"""

helps['cosmosdb sql role assignment create'] = """
type: command
short-summary: Create a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb role assignment create -a MyAccount -g MyResourceGroup -s "/" -p MyPrincipalId -d RoleDefinitionId
"""

helps['cosmosdb sql role assignment delete'] = """
type: command
short-summary: Delete a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Create a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb role assignment delete -a MyAccount -g MyResourceGroup -i RoleAssignmentId
"""

helps['cosmosdb sql role assignment exists'] = """
type: command
short-summary: Checks if an Azure Cosmos DB role assignment exists.
examples:
  - name: Checks if an Azure Cosmos DB role assignment exists.
    text: az cosmosdb role assignment exists -a MyAccount -g MyResourceGroup -i RoleAssignment
"""

helps['cosmosdb sql role assignment list'] = """
type: command
short-summary: List all SQL role assignments under an Azure Cosmos DB account.
examples:
  - name: List all SQL role assignments under an Azure Cosmos DB account.
    text: az cosmosdb role assignment list -a MyAccount -g MyResourceGroup
"""

helps['cosmosdb sql role assignment show'] = """
type: command
short-summary: Show the properties of a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Show the properties of a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb role assignment show -a MyAccount -g MyResourceGroup -i RoleAssignmentId
"""

helps['cosmosdb sql role assignment update'] = """
type: command
short-summary: Update a SQL role assignment under an Azure Cosmos DB account.
examples:
  - name: Update a SQL role assignment under an Azure Cosmos DB account.
    text: az cosmosdb role assignment update -a MyAccount -g MyResourceGroup -b -i RoleAssignmentId -d RoleDefinitionId
"""

helps['cosmosdb table'] = """
type: group
short-summary: Manage Table resources of Azure Cosmos DB account.
"""

helps['cosmosdb table create'] = """
type: command
short-summary: Create an Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table delete'] = """
type: command
short-summary: Delete the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table list'] = """
type: command
short-summary: List the Tables under an Azure Cosmos DB account.
"""

helps['cosmosdb table show'] = """
type: command
short-summary: Show the details of a Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput'] = """
type: group
short-summary: Manage throughput of Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput show'] = """
type: command
short-summary: Get the throughput of the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput update'] = """
type: command
short-summary: Update the throughput of the Table under an Azure Cosmos DB account.
"""

helps['cosmosdb table throughput migrate'] = """
type: command
short-summary: Migrate the throughput of the Table between autoscale and manually provisioned.
"""

helps['cosmosdb update'] = """
type: command
short-summary: Update an Azure Cosmos DB database account.
parameters:
  - name: --locations
    short-summary: Add a location to the Cosmos DB database account
    long-summary: |
        Usage:          --locations KEY=VALUE [KEY=VALUE ...]
        Required Keys:  regionName, failoverPriority
        Optional Key:   isZoneRedundant
        Default:        single region account in the location of the specified resource group.
        Failover priority values are 0 for write regions and greater than 0 for read regions. A failover priority value must be unique and less than the total number of regions.
        Multiple locations can be specified by using more than one `--locations` argument.
examples:
  - name: Update an Azure Cosmos DB database account. (autogenerated)
    text: az cosmosdb update --capabilities EnableGremlin --name MyCosmosDBDatabaseAccount --resource-group MyResourceGroup
    crafted: true
  - name: Creates a new Azure Cosmos DB database account with two regions. UK South is zone redundant.
    text: az cosmosdb update -n myaccount -g mygroup --locations regionName=eastus failoverPriority=0 isZoneRedundant=False --locations regionName=uksouth failoverPriority=1 isZoneRedundant=True --enable-multiple-write-locations
"""
