
# CDK Take Home Assignment

This was my first time using AWS CDK and there was a learning curve in order to understand the product. This required reading the documentation provided in order to understand the syntax.


Issues:
A pain point in trying out AWS CDK was getting the proper environment variables set up. My current setup is Mac OS and I was running node version of 8.X.X.


Explanation of code:
In order to streamline the module installation process, I’ve included all the aws-cdk modules in requirements.txt as it was tedious to run pip install for all of them

There is a basic HTML page on each instance to show a basic web application running. This is created through httpd.sh bash script and will show the hostname of the instance. I’ve commented on the code to give a brief explanation of what is happening.

After running cdk deploy there will be a loadbalance URL that you can click on to see your instances running. 


Ways to improve:

Instead of setting up all my environment variables locally it would have been more efficient to either use Cloud9 or even set this up in a docker container.


The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the .env
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

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

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation




