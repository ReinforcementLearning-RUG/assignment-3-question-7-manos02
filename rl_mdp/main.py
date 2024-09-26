from util import create_mdp, create_policy_1,  create_policy_2
from model_free_prediction.monte_carlo_evaluator import MCEvaluator
from model_free_prediction.td_evaluator import TDEvaluator
from model_free_prediction.td_lambda_evaluator import TDLambdaEvaluator


def main() -> None:
    """
    Starting point of the program, you can instantiate any classes, run methods/functions here as needed.
    """
        
    mdp = create_mdp()
    mcEvaluator = MCEvaluator(mdp)
    tdEvaluator = TDEvaluator(mdp, 0.1)
    tdLambdaEvaluator = TDLambdaEvaluator(mdp, 0.1, 0.5)

    policy1 = create_policy_1()
    policy2 = create_policy_2()

    
    # print(mcEvaluator.evaluate(policy1,1000))
    # print(mcEvaluator.evaluate(policy2,1000))
    
    # print(tdEvaluator.evaluate(policy1, 1000))
    # print(tdEvaluator.evaluate(policy2, 1000))

    # print(tdLambdaEvaluator.evaluate(policy1, 1000))
    # print(tdLambdaEvaluator.evaluate(policy2, 1000))



if __name__ == "__main__":
    main()
