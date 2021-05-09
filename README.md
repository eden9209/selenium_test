<h1>Selenium Python Small Project</h1>
<h3>Goal:</h3>
Design steps case using OOP principle for login page and home page of  <em>"OrangeHRM"</em>  Website.<br>
Practice on writing unit test framework in automotive Testing website

![login_page](https://user-images.githubusercontent.com/73124928/117574350-5da49a80-b0e5-11eb-867a-6181b930b234.png)
<h3>Steps:</h3>

<ol>
  <li>Create a Selenium WebDriver instance</li>
  <li>Configure your browser(In my case Chrome).</li>
  <li>Navigate to the required URL (https://opensource-demo.orangehrmlive.com/).</li>
  <li>Create 3 class : Locators , Pages , Login</li>
</ol>
<h4>Locators class:</h4>
In this class I saved all the html element by id Or Name Or claas . 
<h4>pages class:</h4>
Login page there is 3 methods: write user name , write password , click on the login button. <br>
Home page there is simple method of click on welcome .
<h4>Login class:</h4>
the main file. the aim is to Create instace from Locator and pages class and run the TestCase.

