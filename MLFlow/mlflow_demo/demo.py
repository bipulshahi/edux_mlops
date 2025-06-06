import mlflow
import os
import argparse
import time

mlflow.mlflow.set_tracking_uri("http://127.0.0.1:5000")


def eval(p1,p2):
    output_metric = p1**2 + p2**2
    return output_metric


def main(inp1, inp2):
    with mlflow.start_run(run_name="example_demo"):
        mlflow.log_param("param1" , inp1)
        mlflow.log_param("param2" , inp2)
        metric = eval(p1=inp1, p2=inp2)
        mlflow.log_metric("Eval metric" , metric)
        os.makedirs("dummy", exist_ok=True)
        with open("dummy/example.txt","wt") as f:
            f.write(f"Artifact created as {time.asctime}")
        mlflow.log_artifacts("dummy")




if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--param1','-p1',type=int,default=5)
    args.add_argument('--param2','-p2',type=int,default=10)
    parsed_args = args.parse_args()
    main(parsed_args.param1, parsed_args.param2)