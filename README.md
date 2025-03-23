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

<ul>The Must Haves for the Project:
	<li>The ability for the robot to react to a model detecting an obstacle, mainly by stopping.</li>
	<li>The ability to run GPS laps</li>
	<li>A model for the robot to run</li>
</ul>

<ul>The Nice Haves for the Project:
	<li>The ability to turn around an object based on closeness</li>
	<li>An accurate model that can detect a robocar</li>
	<li>The ability for the car to quickly detect and react to obstacles. </li>
</ul>


</section>

<section>

<h3>Tasks met</h3>

<p>Summary:We managed to get the GPS running on the docker container, along with having the robot react to the model detection. However, we were unable to get those two working together at the same time.</p>



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
<P>The current model implementation requires depthai and the sdk dependencies to be upgraded. In order to get this implementation of the model running, it is recommended to have the model itself run on the donkeycontainer</p>
<p>You need to mount the donkeycar directory inside a new container. When you do so, you need to then check to see if GPS laps can be run in the docker container</p>
<p>The model that was created would be directly imported from roboflow. The detector callback function would return a true false statement, which would decide whether the robot detects it or not.</p>
<p>You would need to import the file that runs the model(in this case the camerausb) and then make some changes to acutator.py.</p>

<p>The implementation relies on the need to have an thread be created. The if statement is there so only one thread is made. The while loop will then set the angle and throttle to 0 in order to stop the robot when the model detects something.</p>

</section>

<section>
<h4>Mechanical documentation</h4>
<image src = "diagram.JPG"></image>
</section>
</body>

<footer>
<h4>Acknowledgements</h4>
<p>Thanks to Professor Jack Siberman and the TA's Alexander, Winston, and Vivekanand.</p>

</footer>
</html>
