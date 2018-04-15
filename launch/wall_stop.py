<launch>
  <include file="$(find pimouse_ros)/launch/pimouse.launch" />
  <node pkg="pimouse_run_corridor" name="wall_stop" type="wall_stop.py" required="true" />
  <test test-name="test_wall_stop" pkg="pimouse_run_corridor" type="travi_test_wall_stop.py" />
</launch>

