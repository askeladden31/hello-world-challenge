# hello-world-challenge
Final challenge of CloudX Associate: GCP Developer, in the absence of Cloud Source Repositories
  
1. Manual Build Docker Image (10 points):  
●	Create a Cloud Source Repository with your app (HTTP Server).
●	Add a Dockerfile file into your repository to build your app.
●	Test the created Docker image.
●	Push the Docker image into the Artifact Repository.
  
(Effective June 17, 2024, Cloud Source Repositories isn't available to new customers. If your organization hasn't previously used Cloud Source Repositories, you can't enable the API or use Cloud Source Repositories. New projects not connected to an organization can't enable the Cloud Source Repositories API.)  
  
	docker build -t us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/hello-world:latest .
	docker run us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/my-gcs-connector:latest
	docker push us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/my-gcs-connector:latest
  
2. Automate Build Docker Image (10 points):
●	Create a pipeline in Cloud Build to build a Docker image when the source code changes.  
  
Configuration: [cloudbuild.yaml](cloudbuild.yaml)  
Trigger configured in Cloud Build Triggers.  
  
3. Manual Docker Image Deployment (10 points):
●	Use the image to create a deployment in Kubernetes.
●	Update the image and apply the change of the deployment.
  
Manifest: [deployment.yaml](deployment.yaml)  
  
	gcloud container clusters get-credentials cluster-1 --zone=us-east1-b
    kubectl apply -f deployment.yaml
	kubectl set image deployments/hello-server hello-world=us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/hello-world:latest
  	
4. Automate Docker Image Deployment (10 points):
●	Create a pipeline in Cloud Build to deploy a new version of your image when the source code changes.
  
Configuration: [cloudbuild.yaml](cloudbuild.yaml)  
Trigger configured in Cloud Build Triggers.  
  
5. Expose your service over Cloud Load Balancer (Ingress) with an external static IP address (10 points)
  
	kubectl expose deployment hello-server --type=LoadBalancer --port 8080
  
6. Connect to Database using Cloud SQL Auth Proxy (10 points):
●	Create a Cloud SQL Database with a private IP address.
●	Connect the Application to the Database over the private IP address using Cloud SQL Auth Proxy.
●	Use Cloud Secret Manager & k8s secrets to store secret data.
  
Cloud SQL Database created in Cloud Console.
Cloud SQL Auth Proxy starts listening in application container ([Dockerfile](Dockerfile)).
  
	gcloud container clusters update cluster-1 --enable-secret-manager --location=us-east1-b
	gcloud secrets create db-password
	gcloud secrets versions add db-password --data-file=password.txt
	kubectl create secret generic db-secret --from-literal=password=$(gcloud secrets versions access latest --secret=db-password)
  
7. Manual SQL migration scripts (see details here https://cloud.google.com/architecture/devops/devops-tech-database-change-management) (10 points):
●	Create and apply SQL database migration scripts using one of database migration tools when the SQL database migration scripts add.
●	Connect the Migration Tool to the Database over the public IP address using Cloud SQL Auth Proxy.
  
Add IP to SQL instance's allowlist.
  
	cloud-sql-proxy resounding-rune-428908-p8:us-east1:sql-instance
	flyway -url=jdbc:postgresql://127.0.0.1:5432/postgres -user=postgres -password=$(gcloud secrets versions access latest --secret=db-password) migrate
  
8. Automate SQL migration scripts (10 points):
●	Create a pipeline in Cloud Build to apply database migration scripts.
  
	docker build -f Dockerfile-migrations -t us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/proxy-migration-image:latest .
	docker push us-east1-docker.pkg.dev/resounding-rune-428908-p8/datalab2/proxy-migration-image:latest
  
Configuration: [cloudbuild-migrations.yaml](cloudbuild-migrations.yaml)  
Trigger configured in Cloud Build Triggers.   
