
# FarOpt
## Fargate based serverless Numerical Optimization

![](./FarOpt.png)

This architecture is a bare bones template of how you can run optimization models in a serverless fashion on Fargate. The Open source SDK can be used to submit optimization tasks and receive logs. 
Fargate will launch the container, run your code, push logs to cloudwatch and exit - you only pay for the seconds that this _optimzation task_ runs. 

Currently supported frameworks inlcude: 

1. PuLP
1. Pyomo
1. OR Tools
1. JuMP (Julia)

## Using the SDK

```python
from faropt
import FarOpt

fo = FarOpt()

fo.configure('../project/src/')

fo.submit()

fo.logs()
```

```html
1598041071123 |  Starting FarOpt backend
1598041071123 | ███████╗ █████╗ ██████╗  ██████╗ ██████╗ ████████╗
1598041071123 | ██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
1598041071123 | █████╗  ███████║██████╔╝██║   ██║██████╔╝   ██║   
1598041071123 | ██╔══╝  ██╔══██║██╔══██╗██║   ██║██╔═══╝    ██║   
1598041071123 | ██║     ██║  ██║██║  ██║╚██████╔╝██║        ██║   
1598041071123 | ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝  
.
.
.
.
.
```

## What's coming up?
1. Scheduling optimization jobs
1. Demand forecasting using Forecast
1. Quantum Approximate Optimization Algorithm
1. SageMaker RL solvers for certain problem types

![](./faropt.png)

# How to use this CDK project

You should explore the contents of this project. It demonstrates a CDK app with an instance of a stack (`faropt_stack`)
which contains an Amazon SQS queue that is subscribed to an Amazon SNS topic.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .env directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
