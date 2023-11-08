import "@azure-tools/typespec-azure-core";
import "@typespec/rest";
import "./models.tsp";

using TypeSpec.Rest;
using TypeSpec.Http;

namespace Microsoft.Purview;

interface PurviewPoliciesOperations {
  @summary("API to list the purview RBAC policies based on a scope")
  @doc("The API lists the Azure purview RBAC policies affecting the scope. The scope can be any valid ARM resource id")
  @route("/{scope}/providers/Microsoft.Purview/policies")
  @get
  List is Azure.Core.Foundations.Operation<
    {
      @doc("The scope of the operation or resource. Valid scopes are: subscription (format: '/subscriptions/{subscriptionId}'), or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'")
      @path
      scope: string;

      @doc("Paging key to paginate to next page.")
      @query("skipToken")
      skipToken?: string;

      @doc("Supported filters : $filter=policyType eq SelfService, $filter=policyType eq SqlDevops. Returns only the policies of the specified type. If not specified, all policies are returned.")
      @query("$filter")
      $filter?: string;
    },
    PolicyList
  >;
}
