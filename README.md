<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, Text-New-Tweets, therealviraat, linkedin_username, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  </a>

  <h3 align="center">Text people new tweets



</h3>

  <p align="center">
    Do your friends not have a Twitter but you still want to share them your hilarious tweets? Look no further! Just set this docker image as a daemon and they'll always be in the loop whenever you tweet!
    <br />
    <br />
    <a href="https://github.com/viraatdas/Text-New-Tweets/issues">Report Bug</a>
    ·
    <a href="https://github.com/viraatdas/Text-New-Tweets/issues">Request Feature</a>

</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project




### Built With

* [python-twitter](https://github.com/bear/python-twitter)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Pipenv 
  ```sh
  pip install pipenv
  ```
Pip should be fine as well. The only package to be installed is `python-twitter`


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/viraatdas/Text-New-Tweets.git
   ```
2. Pipenv environment - or you can use Pip
   ```sh
   pipenv install
   ```

3. Environment file
   ```sh
   mv config_template.py config.py
   ```
4. Access and API tokens for the Twitter API
    - [Instructions](https://python-twitter.readthedocs.io/en/latest/getting_started.html)

5. Update the values in `config.py` accordingly 


<!-- USAGE EXAMPLES -->
## Usage

`python3 send_text.py` 

The code runs every 15 minutes. If there is a new tweet sent, it sends that out otherwise waits 15 minutes again. 

#### Deploy - Example
I decided to use a free EC2 instance. Using the [screen](https://linuxize.com/post/how-to-use-linux-screen/) command, I simply let the code run in perpetuity. 


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/viraatdas/Text-New-Tweets/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Viraat - [@therealviraat](https://twitter.com/therealviraat) - viraat.laldas@gmail.com

README template based on [othneildrew](https://github.com/othneildrew/Best-README-Template)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/viraatdas/Text-New-Tweets.svg?style=for-the-badge
[contributors-url]: https://github.com/viraatdas/Text-New-Tweets/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/viraatdas/Text-New-Tweets.svg?style=for-the-badge
[forks-url]: https://github.com/viraatdas/Text-New-Tweets/network/members
[stars-shield]: https://img.shields.io/github/stars/viraatdas/Text-New-Tweets.svg?style=for-the-badge
[stars-url]: https://github.com/viraatdas/Text-New-Tweets/stargazers
[issues-shield]: https://img.shields.io/github/issues/viraatdas/Text-New-Tweets.svg?style=for-the-badge
[issues-url]: https://github.com/viraatdas/Text-New-Tweets/issues
[license-shield]: https://img.shields.io/github/license/viraatdas/Text-New-Tweets.svg?style=for-the-badge
[license-url]: https://github.com/viraatdas/Text-New-Tweets/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username