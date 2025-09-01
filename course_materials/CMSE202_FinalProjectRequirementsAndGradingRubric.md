# CMSE 202 Final Project: Requirements and Grading Rubric

## Overall requirements

Each project will apply models and/or computational techniques to answer a research question.  Projects will require the following components:

1. **Report**: A report summarizing the question addressed, basic methods applied, results found, and conclusion.

2. **Code**: Code for all methods and results generated. Make sure your instructors can access the repository.

3. **Oral Presentation**: Group presentation with contributions from each group member.

### Report Requirements

The **Report** should be a 400-700 word write-up consisting of a summary of the question(s), methods, results, discussion, and conclusion of your project. The report can be a markdown (.md) file or a PDF.

### Code requirements

All code used for the project should be committed to a **private** GitHub repository for your group that is shared with the instructors. **The code should be well-documented and include a README markdown file (.md) in the GitHub repository that explains how to run the code and a description of what each group member contributed to the overall project**. Well-documented code should include comments to explain what the code is doing and [docstrings](https://en.wikipedia.org/wiki/Docstring) for functions and classes. You should also make sure that the variable names are chosen so that the instructor can make sense of your code.

### Presentation Requirements
Each presentation should be **no more than 10 minutes** long and should include appropriate **visual aids**. The presentation should be **divided roughly evenly between all group members** (i.e. one person shouldn't do all of the talking). **You will give your presentation on the last two days of class**. You are encouraged to practice your presentation in advance to ensure that you stay within the 10-minute limit. Zoom may be a useful tool for practicing your presentation with your group without needing to find a location to meet in person.

Your presentation and report should address:

* The **question(s)** you set out to answer.
* Any **models**, expressed in broad mathematical terms, that you applied to your chosen data or chosen topic.
* The **computational techniques** that you used to analyze your data or run your model. This should include an explanation of any pre-existing python-based libraries or packages that you used to aid in your project.
* The **answer(s)** you arrived at.
* The **difficulties or complications** you ran into with your project and what you did to try to cover overcome these difficulties.


#### Talk slides

It is recommended that you create your slides using Google Slides so that you can more easily collaborate on the slides with your group members, but you are allowed to use another format if there is one that you prefer. Once you've completed your slides, **you should upload a copy of them to D2L using the Project submission folder**. Every member of the group should submit a copy of the slides.

You should aim for having a reasonable number of slides -- a good rule of thumb is ~1 min of time per slide. You should avoid having more than 15 slides for a presentation of this length. In addition, make sure you have enough slides to support your presentation. If you have too few slides you might either have too much content per slide or you don't have enough content in total. **The slides should**:

* Address the above points in a logical order.
* Include a title slide with your project title, name, and course number (with section number).
* Effectively communicate information through a combination of text and figures. Text and figures should be legible (even from the back of the room!).
* Only include text and figures that support the presentation (avoid including content "just because").
* Avoid large paragraphs of text, use bullet points instead.

You may feel compelled to show a live coding demonstration as part of your presentation. While this is perfectly acceptable, you should make sure that you presentation still fits within the **10-minute limit**.


## Grading

The oral presentation, slides, and project code should address all of the points outlined in the "Overall Requirements" above. The project will be graded as follows:

### Presentation
* 25% of the grade (**25 points**) comes from the oral presentation and slides. Is it clear and well-structured? Does the student effectively communicate the key ideas about their results? Do the slides complement their oral presentation, and conform to the guidelines? **10 of the 25 points will come from a peer-review-based "score" of your presentation.** The remaining 15 points will be an instructor-based assessment.

> **Examples of presentation performance**  
> * *Excellent presentation*: student speaks clearly and in a logical manner, and makes their key points clear. They use eye contact and minimally use notes. Slides conform to specifications in final presentation document, including number of slides, adequately addressing all points, legibility. Slides complement oral presentation. (**25 points**)  
> * *Good presentation*: student speaks clearly and logically and conveys key points, but presentation is somewhat lacking (heavy use of notes; moderate eye contact, etc.) Slides deviate from specifications in some minor way: too many or too few slides, not all points addressed, some slides hard to understand (poor graphics, too much or too little text, etc.) (**20 points**)  
> * *Fair presentation*: student's oral presentation is substantially lacking: little eye contact, speaking too quietly to be heard or with little inflection, clarity/logical flow in speaking is sub-par, etc. Slides deviate from specifications in some substantial way: too many or too few slides, half or fewer of points addressed, most slides hard to understand (poor graphics, too much or too little text, etc.)  (**15 points**)  
> * *Poor presentation*: student's oral presentation is completely lacking: little to no eye contact, cannot be heard, there is no logical progression to the presentation. Slides do not conform to specifications in any meaningful way. (**10 points**)  

### Demonstration of content knowledge and computational skills
* 25% of the grade (**25 points**) comes from the content of the abstract, the student's presentation, and in the code developed. Did the students approach a specfic question in a scientific way? Did the students compare and contrast two or three different but appropriate techniques? Are the results (positive or negative!) presented in a clear and convincing manner? This section is subdivided into three categories: abstract summary, computational techniques and visualization.
	* Abstract (**8 pts**): Does the abstract effectively summarize the project?  Is the question clearly presented?  Are basics of methods clear?  Is there a clear conclusion?
	* Computational Tools (**10 pts**): Which tool(s) did you use to solve your problem? Did you use an appropriate tool to answer your scientific question? Your choice of tools should be justified in your presentation.
	* Visualization (**7 pts**): Are your results clearly displayed?  Are the visualizations easy to digest for someone not familiar with the project? Do the visualizations effectively demonstrate some point?

> **Examples of content knowledge and skills demonstration**
> * *Excellent demonstration*: the students pose a specific question with a measureable outcome and use a few different techniques to try to answer the question. The students explain why the chosen techniques are appropriate for answering the proposed question, and compare how the two techniques performed. The graphs are well labeled and helper text is added to the figures to highlight important parts of the figure. (**25 points**)
> * *Good demonstration*: the students pose a specific question with an unclear metric and a few different techniques to try to answer the question, but one of the techniques is not appropriate for the problem. The students briefly explain why they chose the techniques, but do not compare the techniques. The graphs have labeled axes and legends. (**21 points**)
> * *Fair demonstration*: the students use a single technique to try to answer a question that isn't well defined. The students briefly explain why they chose the technique. The graphs simply show raw data or are not labeled. (**12 points**)
> * *Poor demonstration*: the students forego computational tools or perform a superficial analysis and try to answer a poorly-defined question using visualizations and intuition. (**5 points**)

### Collaboration
* 20% of the grade (**20 points**) comes from working together effectively. This grade is individual to each team member.  Team members that worked well with the group will receive a higher grade than students who failed to meet with the group or take on tasks.
	* Balancing the workload: Was the work effectively distributed among all team members? Did each team member contribute meaningfully?
	* Use of collaborative code development tools: Did you leverage version control software to aid in code development between group members? Are your commits descriptive?  Did you manage merge conflicts successfully? Does each team member have at least a few commits (not necessarily in equal quantity)?

> **A component of this collaboration grade will come from a group feedback survey completed by each group member about the group dynamics to get a sense for the overall degree of effective collaboration that took place within the group.**

### Good coding practices
* 30% of the grade (**30 points**) comes from the quality of the code that is written. In addition, your instructor should be able to use the README to understand how to appropriately run your code.
	* A good folder/file structure is essential. You should arrange your files in a systematic way.
	* Does the code have adequate comments? Do the variable names make sense? Do function and classes have Docstrings? Your instructor should be able to read through your code and understand what it is doing and why. Is the data managed effectively and efficiency such that it is easy to understand how the data is being manipulated? Are variables clearly identified? Are appropriate data types used (dictionaries vs. numpy arrays etc.)? Look at past examples of code to get a sense for the level of detail you should include. 
