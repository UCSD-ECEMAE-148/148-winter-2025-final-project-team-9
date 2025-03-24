<html>
<head>
<image src = "logo.JPG" width = 200px height = 200px></image>
<h2>MAE148 Final Project</h2>
<p>Team 9<p>
<image src = "robocar.JPG" width = 300px height = 300px></image>
</head>



<body>
    <section>
        <h3>Team members</h3>
        <li>Dillon Kim:CE major</li>
        <li>Jason Young:MAE major</li>
        <li>Sarena Pham:CE major</li>
        </section>
<section>

<h3>Final Project: Collision Avoidance</h3>

<p>Our goal for the final project was to have an object detection model that would work concurrently with GPS laps. The main idea is that the robocar would race around in a figure 8. While racing, the robot would have a model that would be able to detect obstacles. When an obstacle was detected, it would stop. When the robot no longer was able to detect an obstacle, it would then begin to drive again as normal.</p>



</section>

<section>

<h3>Original Goals</h3>

<p>The original plan was to use an ROS2 implementation. However, due to time constraints, we decided to just modify the internal workings of the donkeycar itself</p>
<p>The Must Haves for the Project:</p>
<ul>
	<li>The ability for the robot to react to a model detecting an obstacle, mainly by stopping.</li>
	<li>The ability to run GPS laps</li>
	<li>A model for the robot to run</li>
</ul>
<p>The Nice Haves for the Project:</p>
<ul>
	<li>The ability to turn around an object based on closeness</li>
	<li>An accurate model that can detect a robocar</li>
	<li>The ability for the car to quickly detect and react to obstacles. </li>
</ul>


</section>

<section>

<h3>Tasks met</h3>

<p>Summary:We managed to get the GPS running on the docker container, along with having the robot react to the model detection. However, we were unable to get those two working together at the same time.</p>

<p>Here is a video of the robocar reacting to the model</p>
<p>https://youtube.com/shorts/jSap0I74En4</p>




</section>

<section>
<h4>Future goals</h4>
<p>I would say a future stretch goal would be to add a functionality that after stopping, forces the robot to move around it. In addition, a more robust model would be appreciated.</p>

</section>

<section>
    <h4>Other Assignments done with the robocar</h4>
    <p>Autonomous lap</p>

    <link>https://youtube.com/shorts/MIYmDNecfd0?feature=share</link>

    <p>GPS lap</p>
    
    <link>https://youtu.be/w0lJrg6fRcE?feature=shared</link>
    <p>OpenCV lap</p>
    <link>https://youtu.be/xnzpPU3z34I?feature=shared</link>
</section>

<section>
<h4>Software documentation</h4>
<P>The current model implementation requires depthai and the dephaisdk dependencies to be upgraded(depthai 2.28, sdk 1.15). In order to get this implementation of the model running, it is recommended to have the model itself run on the donkeycontainer</p>
<p>You need to mount the donkeycar directory inside a new container. When you do so, you need to then check to see if GPS laps can be run in the docker container</p>
<p>The model that was created would be directly imported from roboflow. The detector callback function would return a true false statement, which would decide whether the robot detects it or not.</p>
<p>You would need to import the file that runs the model(in this case the camerausb) and then make some changes to acutator.py.</p>

<p>The implementation relies on the need to have an thread be created. The if statement is there so only one thread is made. The while loop will then set the angle and throttle to 0 in order to stop the robot when the model detects something.</p>

</section>

<section>
<h4>Mechanical and Electrical documentation</h4>
<image src = "newdiagram.JPG"></image>
<p>Electrical Diagram Revised Explanation: The RoboCar or robot car is connected to a power supply in the form of a LiPo battery of at least 14.8 V that provides power to the entire car. The distribution of power across the entire car can be controlled with the VESC switch that powers on or off the car. When the VESC switch is turned on, current flows through the anti-spark switch that prevents sparking of the car, and then into the buck converter that steps down the DC voltage to a safe level. The DC-DC buck converter is crucial in protecting all hardware components of the car, preventing overflow of current causing a short in the entire car that would cease the car's ability to function. The DC barrel jack redirects stepped-down current coming out from the buck converter to the Jetson, allowing the Jetson to turn on. The Jetson then powers the GPS Nav1, the OAK-D camera, and the VESC steering control. The Jetson itself allows the car to collect signals from the Earth to determine location accurately, to see objects in front of the car, and to power the steering control that helps drive and turn the car. The motor or throttle of the car provides engine power to the VESC steering control, enabling the car to move forwards, backwards, and steering motions.</p>
<p>Orange lidar mount:https://cad.onshape.com/documents/ac0c79804f0119ca016675cd/w/fb4d21fe24ad051bae48313e/e/ca930eb42fde4e6012a60675?renderMode=0&uiState=67e05ebe48d9c8025a8743b5</p>
<p>Green camera holder:https://cad.onshape.com/documents/681a28c8048787a752c53829/w/c6ccd98731fac958f389a55a/e/18c55d35ca7f74e7667ec29d?renderMode=0&uiState=67e05e775fa55176d8f6e7b8 </p>
<p>Wood base plate:https://cad.onshape.com/documents/ac0c79804f0119ca016675cd/w/fb4d21fe24ad051bae48313e/e/f52265452eab760c9278867b?renderMode=0&uiState=67e05f0748d9c8025a874474</p>


</section>
</body>

<footer>
<h4>Acknowledgements</h4>
<p>Thanks to Professor Jack Siberman and the TA's Alexander, Winston, and Vivekanand.</p>

</footer>
</html>
