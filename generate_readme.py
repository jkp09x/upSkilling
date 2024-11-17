#!/opt/anaconda3/bin/python3

import json

with open('certifications.json', 'r') as file:
    certifications = json.load(file)

# Function to generate badge url
def get_badge(platform):
    platformDict = {
        "coursera": "![Coursera](https://img.shields.io/badge/Coursera-%230056D2.svg?style=for-the-badge&logo=Coursera&logoColor=white)",
        "datacamp": "![Datacamp](https://img.shields.io/badge/Datacamp-05192D?style=for-the-badge&logo=datacamp&logoColor=03E860)",
        "udacity": "![Udacity](https://img.shields.io/badge/Udacity-grey?style=for-the-badge&logo=udacity&logoColor=15B8E6)",
        "udemy": "![Udemy](https://img.shields.io/badge/Udemy-A435F0?style=for-the-badge&logo=Udemy&logoColor=white)"
    }
    if platform.lower() in platformDict:
        return platformDict[platform.lower()]
    elif platform.lower() == "udacity":
        return "![Udacity Badge](https://img.shields.io/badge/Udacity-Nanodegree-green)"
    elif platform.lower() == "udemy":
        return "![Udemy Badge](https://img.shields.io/badge/Udemy-Certification-purple)"

# Function to generate course
def get_course_title(cert):
    if ({cert['institution']} == {cert['platform']}):
        return f" **[{cert['title']}]({cert['course_link']})** - *{cert['institution']}*  "
    else:
        return f" **[{cert['title']}]({cert['course_link']})** - *{cert['institution']}, {cert['platform']}*  "

# Generate skills icons based on string.
# Badges sourced from https://ileriayo.github.io/markdown-badges/#markdown-badges
# Skills list to remain ascending alphabetical order based on string searched (c++, maven etc.)
def get_skills(skills):

    # Error check if skills is empty
    if not skills:
        return f" N/A "

    skillsDict = {
        "bash": "![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)",
        "c++": "![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)",
        "cmake": "![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white)",
        "git": "![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)",
        "github": "![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)",
        "jenkins": "![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white)",
        "linux": "![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)",
        "maven": "![Apache Maven](https://img.shields.io/badge/Apache%20Maven-C71A36?style=for-the-badge&logo=Apache%20Maven&logoColor=white)",
        "python": "![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)",
        "vim":"![Vim](https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white)",
    }

    # Convert all strings to lower case
    skills = skills.lower()

    # Convert string to list
    skillsList = skills.split()
    skillsList.sort()

    skillStr = ""
    for skill in skillsList:
        # Add known skill badges
        if skill in skillsDict:
            skillStr += skillsDict[skill]
        # Add skill text if no badge available
        else:
            skillStr += skill
        skillStr += " "

    return f" {skillStr} "

# Generate README content
readme_content = "# My Certifications\n\n"

readme_content += f" | Course Name (URL) | Online Platform | Completion Date (Cert. Link) | Skills Learned |\n"
readme_content += f" | :---------------- | :-------------- | :--------------------------- | :------------- |\n"
for newCert in certifications:
    if "In-Progress" == newCert['completion_date']:
        readme_content += f" | [{newCert['title']}]({newCert['course_link']}) | {get_badge(newCert['platform'])} | {newCert['completion_date']} | {get_skills(newCert['skills_learned'])} |\n"
    else:
        readme_content += f" | [{newCert['title']}]({newCert['course_link']}) | {get_badge(newCert['platform'])} | [{newCert['completion_date']}]({newCert['certification_link']}) | {get_skills(newCert['skills_learned'])} |\n"


# Write to README.md
with open('README.md', 'w') as file:
    file.write(readme_content)

print("README.md generated successfully.")
