# BLD Devs

The project is a personal web page where I expose my professional background. The implementation is simple enough, to keep the scope of the project under control. I wanted to do a project like this to broaden my knowledge of Python and techniques like integrating JavaScript scripting, algorithms in python, etc.

Technologies used:

   * Python 3.9
   * Flask
   * Flask-wtf
   * Flask-Mail
   * Flask-Talisman
   * wtforms
   * HTML5
   * CSS
   * JavaScript


# Stages of construction

Hello everybody,

Today I will tell you about my python application which is based on the flask framework.

I was able to use several objects related to flask like flask-mail, flask-wtf or even flask-talisman.
I started with the background, a JavaScript script that particularly interested me for its aesthetics.
I continued with the integration of the navigation bar and the bootstrap footer. I was able to give it an absolute position to cover the background and then give it the color "transparent".
The background is therefore visible in the navigation bar and the footer. The desired objective was therefore achieved.
At this present stage, I therefore had a perfect layout for all my pages. :smiling_face_with_three_hearts:

I found a css animation that particularly inspired me for my home page. I was able to modify the animation according to my wishes.
Just like the “CONTACT” button, it has an effect: hover.

So I researched on the internet how to make a mail form that sends an email with flask-Mail and flask-wtf. The set-up was easier than I expected.

Once functional, I integrated the Google recaptcha module, in order to avoid spam.

After that I went to the deployment part on the heroku hosting and I also reserved a domain name on OVH.
I find that the compatibility between the two providers is not ideal and far from practical. :hot_face:

After the deployment, I therefore imported flask-talisman, which formed me many securities. During deployment, nothing was displayed.
They were already blocked by talisman's strict security settings.

After configuring the talisman correctly and securing my SSL certificate on the heroku host, my site is ready and ready to receive from the public.

I have 2-3 pages left to complete, this is my "CV", with my experiences, skills, portfolio etc.
I do not yet complete them, I can do it during my job search, after my training.

Thanks for reading me,

Goodbye, :hugs:

It was CS50


# How to launch application


   1. Check that you have Python 3.9
   2. Clone the code: `git clone https://github.com/kroos783/bld-devs.git`
   3. Run command prompt in the folder and run `pip install requirements.txt`  to install all dependencies
   4. Once installed run command `flask run` 
   5. In your browser go to localhost:5000
   6. You are ready to go!
