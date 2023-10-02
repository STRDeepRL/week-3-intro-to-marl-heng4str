from multigrid.agents_pool.YourName_policies.YourPolicyName_policy_v2 import YourPolicyNameV2_Policy
from multigrid.agents_pool.YourName_policies.YourPolicyName_policy import YourPolicyName_Policy

from multigrid.agents_pool.Heng_policies.Heng_policy_v2 import HengV2_Policy
from multigrid.agents_pool.Heng_policies.Heng_policy import Heng_Policy

from multigrid.agents_pool.Blather_policies.Blather_policy_v2 import BlatherV2_Policy
from multigrid.agents_pool.Blather_policies.Blather_policy import Blather_Policy

# from multigrid.agents_pool.JaiAslam_policies.YourPolicyName_policy_v2 import YourPolicyNameV2_Policy as 
from multigrid.agents_pool.JaiAslam_policies.YourPolicyName_policy import YourPolicyName_Policy as JaiAslam_policies

from multigrid.agents_pool.JamesStankowicz_policies.Default_policy import DefaultPolicy
from multigrid.agents_pool.JamesStankowicz_policies.Eliminator_policy import EliminatorPolicy
from multigrid.agents_pool.JamesStankowicz_policies.PickUpper_policy import PickUpperPolicy


SubmissionPolicies = {
    "JaiAslamAgent": JaiAslam_policies,
    "jpblackburn_policy": YourPolicyName_Policy,
    # "your_policy_name_v2": YourPolicyNameV2_Policy,
    "heng_policy": Heng_Policy,
    # "heng_policy_v2": HengV2_Policy,
    "blather_policy": Blather_Policy,
    # "blather_policy_v2": BlatherV2_Policy,
    # "JaiAslam_policy": YourPolicyNameV2_Policy,
    # "JaiAslam_policy_v2": YourPolicyName_Policy,
    # "default": DefaultPolicy,
    # "eliminator": EliminatorPolicy,
    "pickupper": PickUpperPolicy,
}
