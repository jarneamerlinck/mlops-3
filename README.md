# Automated unit testing with Github Actions and Docker
Okay, we now have an automated pipeline which will run each time new, raw data is pushed to the repository.  
We're a step closer to using good CI/CD practices, but we're not there yet.

A big part of CI/CD is using automated unit tests, which check that your code behaves exactly the way it is expected to behave.  
For Machine Learning, we're especially interested in ensuring that our data still looks exactly like we expect.
We'll now write two simple, automated data-centric unit tests which will do exactly that.

## Theory

If we want to write customized unit tests which will run using Github Actions, we're going to need some new actions to run from inside our workflows.
If we want to use a Github Action, we can either:
1. Look for the thing we want to do on the Github Actions Marketplace
2. Write our own customized action

Since it's extremely doubtful that exactly the unit test we want to write which will work on our exact datasets exists in the Marketplace, we have no other choice than to write our own custom action here.

Actions are written in either Python or Javascript, and should be placed under the ./.github/actions folder. Actions need four specific types of files:
1. The **action.yml** file itself. This is what Github uses to know that this folder is an action and gives some information on how to run the action.
2. A **Dockerfile**, which specifies what our containers (read: environment) should look like.
3. An **entrypoint.sh**, to direct our docker container on how to run our script.
4. And finally, our unit test itself, in the form of a **javascript or python file**.
5. Optionally, we can provide a **requirements.txt** file as well so our Docker image knows which packages to install into the container.

More information on Docker can be found here: https://www.docker.com/  
More information on Github Actions can be found here: https://docs.github.com/en/actions?msclkid=0d5d279ea7db11eca293eb1915baf22e

## Exercises

I already wrote one new workflow called 'unittest_input' which will run each time new data is pushed to our *data/raw* folder.  
This workflow will use a custom action that I wrote, which will ensure that our dataframe columns haven't changed with new data coming in.

Now it's up to you to write your own action. I want you to write a unit test that automatically checks whether our predictions are still either 0 or 1 each time new data is pushed to the *data/output* folder, i.e. the results of our *inference.py*.
1. Clone this repository to your own github account by using the 'Use this template' button.
2. Look at the workflow and action that I wrote and make sure you understand them.
3. Create a new workflow which reacts to a push event in the required folder. Commit this to a new branch as before and create a merge request.
4. Write a step (in a job) in your workflow which redirects towards a custom action you'll write called 'unittest_output'
5. Go to the *.github/actions* folder and create an action called 'unittest_output' with a python unittest that has our wanted behavior.
6. Change our RandomForrestClassifier model to a LinearRegression model (don't forget to import sklear.linear_models for this) and temporary comment out the calculation of the accuracy metrics. Run the inference.py script again. Will our unit test fail? Why is that? If we insisted on using a Linear Model here, which model should we have used instead?

## Next up

When you're finished, we'll continue our session in the next repository: https://github.com/LukasMahieuArinti/mlops-4

The solution can be found there as well.
