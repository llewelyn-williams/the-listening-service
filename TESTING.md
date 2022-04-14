# Testing


## PEP8 Standard Linters
### Expected
The code is expected to pass without any major issues highlighted.
### Test
python3 -m flake8 command run to see flake8 error warnings
### Result
Frequent checking throughout development revealed many training whitespaces, missing newlines, extra newlines and lines too long that were fixed along the way.
At the end of the project the only errors showing were ones from code that was not written my myself, so they were left as they were in case they were deliberately that way for a reason.


## WC3 Markup Validation 
### Expected
The site is expected to pass validation with no errors.
### Test
I supplied the Live Heroku address of the site to [The WC3 Markup Validation Service](https://validator.w3.org/) and ran the test.
### Result
![HTML Validation Errors](assets/readme-images/html-validation-errors.png)  
THe first error I attempted to fix by enclosing the li tag within ul tags, however this piece of code being a bootstrap component, doing so broke the functionality of it.
The second error of duplicate id is related to using different navigation for different size screens.
### Fix
Renaming one of the duplicate ids.
### Unresolved
As the first bakes the functionality it will be left for now until a solution can be found that removes the error but doesn't break the functionality.



## Responsiveness
### Expected
Throughout the different sections the design should remain well laid out regardless of the device size
### Test
Using Google Developer Tools I changed to each device available to see how the layout out looked, as well as using the "responsive" layout and changing the shape and size of the viewport with the drag handles. I did this repeatedly during the development process and again at the end.
### Result
...
### Fix
...


## Functionality
### Expected
That the user will be able to navigate and perform CRUD actions without experiencing errors.
### Test
...
### Result
...
### Fix
...


## Performance
### Expected
For the site to load quickly.
### Test
Using Lighthouse from Chrome Developer tools.
### Result
![Lighthouse Performance Report](assets/readme-images/performance.png)  
...
### Unresolved
...
 
 
## Accessibility
### Expected
The site should not have any major accessibility issues as shown by accessibility tests.
### Test
Using Lighthouse from Chrome Developer tools.
### Result
 ![Lighthouse Accessibility Report](assets/readme-images/accessibility.png)  
...
### Fix
...
### Unresolved
...
 
## SEO
### Expected
No major issues to show from SEO report.
### Test
Using Lighthouse from Chrome Developer tools, I ran a report.
### Result
 ![Lighthouse SEO Report](assets/readme-images/seo.png)  
...
### Fix
...
 
## Usability
### Expected
That users should be able to use the site intuitively 
### Test
Throughout development I checked the navigation pathways throughout site.
### Result
...
### Fix
...
### Unresolved
...