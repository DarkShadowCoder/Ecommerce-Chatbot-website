# Ecommerce-Chatbot-website
Projet de creation d'un site e-commerce de produits en tout genre avec integration d'un chatbot <br>
<p>
	<img alt="Static Badge" src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
	<img alt="Static Badge" src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white">
	<img alt="Static Badge" src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white">
</p>
<img src="service/docs/imgs/ecommerce.jpg" alt='image de site ecommerce' width="1000px" height="400px">
 <h2 style="text-align:center">Table de contenu</h2>
 <ol style="border-radius:20px;font-size:22px;background-color:whitesmoke;display:flex;flex-direction:column;justify-content:center;align-items:center">
   <li><a href="">Description du projet</a></li> 
   <li><a href=""> Architecture du site web</a></li>
   <li><a href=""  >Deep-learning: Chatbot</a></li>
   <li><a href="">Integration du chatbot</a>  </li>
   <li> <a href="">Interface graphique</a></li>
   <li> <a href="">Installation et utilisation</a></li>
   <li> <a href="">Credits</a> </li>
 </ol>
<h2>Description du projet</h2>
<div style="border-left:15px solid red; padding-left:25px;border-bottom: 2px solid gray;padding:8px;border-radius:5px;border-right:2px solid gray; text-align:justify">Il s'agit ici d'un site web moderne crée en utilisant les langages de programmmation python et React concus grace à une architecture microservice et admettant plusieurs services autonomes et deployés sur le cloud (Amazone EC2);
Parmis les differents services et outre que les services de base d'un site de vente en ligne. Ce site web admet un service de de payment bancaire architecturé suivant le diagrammes ci-dessous. Aussi, ce site web contient un systeme d'assiance virtuelle: Un chatbot pour gerer les differentes transactions et/ou opérations en mode discussions.
A cela s'ajoute un systeme d'analyse intelligente des differents utilisateurs integré à la page de suivie d'utilisateurs geré par l'administrateur.
<br/>
Le site web est concus grace à <strong style="color:blue">flask</strong> en backend;<br>
L'interface utilisateur est crée avec le framework <strong style="color:blue">React</strong>;
<br>
Nous utilisons <strong style="color:blue">MongoDB (NoSQL) </strong> pour la gestion de la base de données.
<br><strong style="color:blue">Docker</strong> nous permet d'"empaqueter" les differents services ;
<br> L'orchestration des conteneurs est gerée grace à <strong style="color:blue">Kubernete </strong>;<br>
Le site web est deployé sur <strong style="color:blue">Amazone EC2</strong> qui represente ici un service;
<br> Le chatbot est concus avec python en utilisant des algorithmes de Deep Learning : NLP avec <strong style="color:blue">Tensorflow et SQlearn</strong>
;<br> Le systeme d'analyse des données utilisateurs est egalement cré avec de <strong style="color:blue">python (SQlearn) </strong> 
</div>

<h2>Architecture du site web</h2>

<h2>Deep-learning: Chatbot</h2>

<h2>Integration du chatbot</h2>

<h2>Interface graphique</h2>

<h2>Intallation et utilisation</h2>
<h3><ol><li>A partir de Docker</li> </ol> </h3>
	<p>Docker. Docker est un logiciel qui permet de créer et de gérer des conteneurs, qui sont des environnements isolés pour exécuter des applications. Pour installer Docker, vous devez suivre les étapes suivantes, selon votre système d’exploitation:</p><br>
<li>Si vous utilisez Windows 10 ou 11, vous devez télécharger le fichier d’installation Docker pour Desktop sur le Docker Hub12, lancer l’installation en tant qu’administrateur, activer les fonctionnalités Hyper-V Windows et lancer Docker.</li>
<li>Si vous utilisez Windows 10 ou 11, vous devez télécharger le fichier d’installation Docker pour Desktop sur le Docker Hub12, lancer l’installation en tant qu’administrateur, activer les fonctionnalités Hyper-V Windows et lancer Docker.</li>
	
	sudo apt update
 	sudo apt install apt-transport-https ca-certificates curl software-properties-common
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add 
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
	sudo apt update
	sudo apt install docker-ce
 <p>Pour consulter le site web , telecharger l'image docker du projet qui sont des fichiers contenant les divers services de l'applications.Dans l'invite de commande, éxecuter la commande suivante:
 	
	 docker pull test-driven-app
  <br> Pour executer le conteneur, inserer la commande:

  	docker run -it test-driven-app
 </p>

 <h3><ol><li>Grace à l'environnement virtuel</li> </ol></h3>
 <li>Telecharger le projets dans votre machine grace à la commande git:
 	
	 git clone https://github.com/DarkShadowCoder/Ecommerce-chatbot-website.git
  	 cd Microservices-with-Docker-flask-and-react
 </li>
 <li>Ensuite activer l'environnemnt virtuel grace à la commande:
 	
	 source ./env/bin/activate
 </li>
 <li>Installer toutes les librairies requise pour executer l'application grace à:
	
  	pip install -r requirements.txt
 </li>
 <li>Executer le code avec:

 	npm start
 </li>
<h2>Credits</h2>
<h3>Langages utilisés</h3>
	<p>
		<img alt="Static Badge" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  		<img alt="Static Badge" src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
		<img alt="Static Badge" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
		<img alt="Static Badge" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
	</p>
 <h3>Me contacter</h3>
 <p>
	 <img alt="Static Badge" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/Quora-%23B92B27.svg?&style=for-the-badge&logo=Quora&logoColor=white">
	 <img alt="Static Badge" src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white">
 </p>
	
</div>
