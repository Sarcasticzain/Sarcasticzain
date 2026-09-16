<div align="center">
  <!-- Profile Avatar & Branding -->
  <a href="https://github.com/Sarcasticzain">
    <img src="https://avatars.githubusercontent.com/u/123839861?v=4" width="130" height="130" style="border-radius: 50%; border: 3px solid #61AFEF;" alt="Zain's Avatar" />
  </a>

  <br/><br/>

  <!-- Animated Typing Header -->
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=61AFEF&center=true&vcenter=true&width=600&lines=Hi+There!+I'm+Zain+Ul+Arfeen;The+Sarcastic+Developer;Full-Stack+%26+WebSec+Developer;Content+Creator+%26+Tech+Explorer" alt="Typing SVG" />
  </a>

  <p><b>🚀 Turning coffee into code, bugs into version control, and sarcasm into full-stack web apps</b></p>

  <!-- Quick Badges -->
  <p>
    <a href="resume.pdf" target="_blank">
      <img src="https://img.shields.io/badge/📄_Download-Resume-FF4B4B?style=for-the-badge&logoColor=white" alt="Resume"/>
    </a>
    <a href="https://github.com/Sarcasticzain">
      <img src="https://img.shields.io/github/followers/Sarcasticzain?label=Followers&logo=github&style=for-the-badge&color=238636" alt="GitHub Followers"/>
    </a>
    <img src="https://komarev.com/ghpvc/?username=Sarcasticzain&style=for-the-badge&color=0e75a0&label=Profile+Views" alt="Visitor Counter" />
  </p>
</div>

<hr/>

## 👨‍💻 About Me

> **⚡ Quick Overview**
> * 💻 **Known As:** Sarcastic Developer
> * 🛠️ **Focus:** Full-Stack Web Apps, Security Analysis Tools & Interactive UIs
> * 🔍 **Currently Building:** WebSec PRO v3.0 & Web-based utilities
> * 🎥 **Content Creation:** Tech videos, tutorials, and hot takes on YouTube & Socials
> * 💬 **Ask me about:** Web Development, Cybersecurity Recon, JavaScript & UI Engineering
> * ⚡ **Motto:** Built with sarcasm & questionable life choices ✦

<hr/>

## 🏆 Competitive Programming & Coding Platforms

<p align="center">
  <a href="https://leetcode.com/Sarcasticzain" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode"/>
  </a>
  <a href="https://www.codechef.com/users/Sarcasticzain" target="_blank">
    <img src="https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef"/>
  </a>
  <a href="https://www.geeksforgeeks.org/user/Sarcasticzain" target="_blank">
    <img src="https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks"/>
  </a>
  <a href="https://www.hackerrank.com/Sarcasticzain" target="_blank">
    <img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white" alt="HackerRank"/>
  </a>
</p>

<div align="center">
  <a href="https://leetcode.com/Sarcasticzain">
    <img src="https://leetcard.jacoblin.cool/Sarcasticzain?theme=tokyonight&font=Fira%20Code&ext=activity" alt="LeetCode Stats" />
  </a>
</div>

<hr/>

## 🛠️ Tech Stack & Skills

<div align="center">

**Frontend & UI Development**<br/>
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=html,css,js,ts,react,tailwind,bootstrap" alt="Frontend Skills" />
</a>

<br/>

**Backend, Security & Databases**<br/>
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=nodejs,express,postgres,mongodb,python,cpp" alt="Backend Skills" />
</a>

<br/>

**Tools & Environment**<br/>
<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,github,vscode,figma,postman,linux" alt="Tools Skills" />
</a>

</div>

<hr/>

## 🚀 Featured Web Apps & Projects

### 🛡️ [WebSec PRO v3.0](https://github.com/Sarcasticzain/WebSec-PRO)
Comprehensive web security and recon suite featuring Port Scanning, WHOIS lookup, Tech Stack Detection, Malware DB checking & Cookie Deep Dive.
* **Tech:** <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" /> <img src="https://img.shields.io/badge/Security-00F5A0?style=flat-square&logo=shield&logoColor=black" />
* **Links:** [View Repository](https://github.com/Sarcasticzain/WebSec-PRO) | [Launch App](WebSec.html)

### 🌤️ [Whaather v3](https://github.com/Sarcasticzain/Whaather-v3)
Sleek, real-time weather forecasting application designed for instant updates without requiring client-side API key configuration.
* **Tech:** <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" /> <img srcIt looks like the alignment for the main stats card is spot on! However, the "GitHub Stats" and "Top Languages" links in `image_aef70a.png` currently look like standard text with a forced background color and default underlines. This clashes with the sleek dark theme of your dashboard. 

To fix this, you should style them as proper toggle buttons or tabs, removing the default underline and giving them some breathing room with padding. 

Since you are working with a dark-themed dashboard, here is how you can style them cleanly using **Tailwind CSS**. 

### The Solution: UI Tabs
You can create a distinct "active" state for the tab you are currently on, and an "inactive" state for the other one.

```html
<div class="flex justify-center space-x-2 mb-6">
  <!-- Active Tab (e.g., GitHub Stats) -->
  <button class="px-4 py-2 bg-gray-800 text-blue-400 rounded-md text-sm font-semibold shadow-sm border border-gray-700 transition-colors">
    GitHub Stats
  </button>
  
  <!-- Inactive Tab (e.g., Top Languages) -->
  <button class="px-4 py-2 bg-transparent text-gray-400 rounded-md text-sm font-medium hover:text-gray-200 hover:bg-gray-800 transition-colors">
    Top Languages
  </button>
</div>
