
# SyllabusStripper

## Hackathon Submission for Hello World 2020
### Team *Sons of Kedar*
// insert website link here

// insert devpost link here

## Inspiration

Syllabus Stripper is inspired by that annoying ritual we all do at the beginning of the semester of setting up our calendar. We hate it, so do you. No one wants to spend hours going through syllabus after syllabus creating event after event while we could be doing much more important things. Syllabus Stripper is here to expedite that process. 

## What it does
In order to simplify the process, Syllabus Stripper allows students to give us their syllabi and let us handle the dirty work.

With the simple user interface, students can easily upload their syllabus in either docx, doc, or pdf formats and download an iCalendar file they can import into their virtual calendars containing important information from the class.

## How we built it
To create Syllabus Stripper, we used a combination of [Arjun's job to fill this in] to implement the frontend side of the web-app. With the backend side, we utilized [Fill this in later after we have everything done].

Additionally, we used GitHub for source control and some intense L33T whiteboard drawing to collaboratively discuss our ideas.

We also used widely available Python libraries such as flask, tabula, PyPDF2, textract, and dateutil to make the code readable and more efficient.

## Challenges we ran into

[Do this later retrospectively]

It's not inherently obvious how to take data from PDFs, docx, and doc and extract events out of it. We spent a large portion of the hackathon getting from this pipeline to work effectively. A lot of time was sunk into:

Parsing through different file types differently
Creating a robust date detection system for detecting and extracting events (Thanks regex !)
Inconsistent formatting for pdfs meant we needed a broad reaching solution to parse data.
Integrating the front end to the back end also had a host of other problems. None of us were experienced in doing this, and the last few hours was spent fighting the smallest errors.

## Accomplishments that we're proud of
[Do later]

## What we learned
**Arjun**:  I learned a LOT through this experience! Usually, I am the type of person that has ideas and starts projects easily, but when large errors occur that cause me to scale-down my ideas, I get discouraged easily. Participating in this hackathon taught me to become more tenacious when dealing with coding projects and to have the patience to push onwards and seek help even when things may seem impossible. On a more technical note, I learned a lot more about HTML and CSS, and I hosted a new server than what I'm used to. I usually use Apache and PHP when hosting servers, but today I got to experience working with the python language and utilizing Spyder to handle my pip imports while I work on my project. Furthermore, we hosted using Flask, which I was completely unfamiliar with until now. Finally, I gained a lot more experience in python as I was actually able to work on a project with many modules involved.

**Bryan**:   I normally stray away from larger projects, due to feeling lost on what to do. While this project was no different, I learned to at least persevere during the confusion, even if it lasts throughout the competition. Before the competition, I had little experience in python, and managed to at least figure out the basics in time to get by. A lot of my time was spent scraping the texts, and familiarizing myself with pdf, and docx libraries in order to read in user info, regardless of it was in a table or not. I also learned a lot about Regex, and was a primary tool for parsing dates.

**Jacob**:

**Jeongbin**: I leanred how to improve from failures. I have attempted to employ natural language processing, tesnorflow--machine learning, and OCR. Since I am new to coding and there were some descrepancies among our codes, I was able to actually learn how things really work at least in a basic level. Also, I reviewed a bit of python and a way how to integrate the local serval to the python code and the website, using Flask.


## What's next for Syllabus Stripper

[Talk about future plans and how we can improve upon this project further]

- Apply more effective models to get a lower error on extracting events
- Support more file types?
- Idk add more later lul
