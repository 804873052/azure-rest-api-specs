import "@typespec/rest";
import "@typespec/http";
import "@azure-tools/typespec-azure-core";
import "@azure-tools/typespec-azure-resource-manager";

using TypeSpec.Rest;
using TypeSpec.Http;
using Azure.ResourceManager;
using Azure.ResourceManager.Foundations;

namespace Microsoft.Purview;

interface Operations extends Azure.ResourceManager.Operations {}

enum ObjectType {
  User,
  Group,
  ServicePrincipal,
}

enum Decision {
  Permit,
  Deny,
}

enum CreatedByType {
  User,
  Application,
  ManagedIdentity,
  Key,
}

enum Origin {
  user,
  system,
  `user,system`,
}

enum ActionType {
  Internal,
}

@doc("A paginated list of purview RBAC policies")
model PolicyList is Azure.Core.Page<Policy>;

@doc("Purview RBAC policy")
model Policy {
  // ...ProxyResource;
  ...ArmResource;

  @doc("The policy kind")
  kind?: string;

  @doc("The policy source")
  source: string;

  @doc("The etag version of a policy")
  etag: string;

  @doc("Array of scopes where the policy is published")
  scopes: string[];

  @doc("Members of the policy")
  members: PolicyMembers;

  @doc("Array of decision rules for the policy")
  decisionRules: PolicyDecisionRule[];

  @doc("The timestamp of the expiry time of the policy (UTC).")
  // FIXME: (utcDateTime) Please double check that this is the correct type for your scenario.
  expiryTime?: utcDateTime;

  @doc("The AAD member who requested the policy")
  requestor?: string;
}

@doc("Policy member")
model PolicyMembers {
  @doc("Array of azure active directory members")
  fabricItemMembers?: FabricItemMember[];

  @doc("Array of azure active directory members")
  aadMembers?: AADMember[];
}

@doc("Microsoft fabric item member")
model FabricItemMember {
  @doc("Source path of the member")
  sourcePath?: string;

  @doc("Array of access items for the member")
  itemAccess?: string[];
}

@doc("Azure active directory member")
model AADMember {
  @doc("The tenantId of the member")
  tenantId?: string;

  @doc("The objectId of the member")
  objectId?: string;

  @doc("The objectType of the member.")
  objectType?: ObjectType;
}

@doc("Purview RBAC policy decision rule")
model PolicyDecisionRule {
  @doc("The effect for rule")
  effect: Decision;

  @doc("Array of attribute predicates")
  permission?: AttributePredicate[];
}

@doc("Attribute predicate for a policy permission")
model AttributePredicate {
  @doc("AttributeName of a policy permission")
  attributeName?: string;

  @doc("values for a policy permission")
  attributeValueIncludedIn?: string[];
}
