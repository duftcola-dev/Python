
Flask app + mysql
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

ATENTION USER ! 
    **In order to work this app requires the following deppendencies  :
        - Docker 
        - Docker-Compose
        - Npm
        - Python >=3.8
        - Make
    
    ** This app has been tested in a linux-ubuntu-focal:20 environment

    **Once these deppendencies are installed in your machine run the following command :

        - make install  ** this will install all the packages this app needs to run
        - make run  **launches the the containers where the app run
        - make show ** diplays the container running
        - make test ** runs unitary test with postman and newman ** results are displayed in the console
        - make flush ** deletes all images and volumens created by <make install> 
        *** notice the database takes about 20-30 seconds to be ready , so running the test too soon may raise the error that 
        flask cannot connect to mysql ***

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This backend app pocesses the following endpoints: 

    /status : ** returns the server and database status  (OK or NO_OK)
    /get_vehicles : returns all the vechiles registered in the database
    /get_vehicle : returns a vehicle based on its "batch"
    /update_vehicle_state : updates the vehicles id_state according with their speed ** Check init.sql  to know how the database is created ** 
    /get_positions : returns all the postions stored in the database 
