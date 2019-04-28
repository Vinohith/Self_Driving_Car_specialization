#!/usr/bin/env python3

"""
2D Controller Class to be used for the CARLA waypoint follower demo.
"""

import cutils
import numpy as np

class Controller2D(object):
    def __init__(self, waypoints):
        self.vars                = cutils.CUtils()
        self._current_x          = 0
        self._current_y          = 0
        self._current_yaw        = 0
        self._current_speed      = 0
        self._desired_speed      = 0
        self._current_frame      = 0
        self._current_timestamp  = 0
        self._start_control_loop = False
        self._set_throttle       = 0
        self._set_brake          = 0
        self._set_steer          = 0
        self._waypoints          = waypoints
        self._conv_rad_to_steer  = 180.0 / 70.0 / np.pi
        self._pi                 = np.pi
        self._2pi                = 2.0 * np.pi

    def update_values(self, x, y, yaw, speed, timestamp, frame):
        self._current_x         = x
        self._current_y         = y
        self._current_yaw       = yaw
        self._current_speed     = speed
        self._current_timestamp = timestamp
        self._current_frame     = frame
        if self._current_frame:
            self._start_control_loop = True

    def update_desired_speed(self):
        min_idx       = 0
        min_dist      = float("inf")
        desired_speed = 0
        for i in range(len(self._waypoints)):
            dist = np.linalg.norm(np.array([
                    self._waypoints[i][0] - self._current_x,
                    self._waypoints[i][1] - self._current_y]))
            if dist < min_dist:
                min_dist = dist
                min_idx = i
        if min_idx < len(self._waypoints)-1:
            desired_speed = self._waypoints[min_idx][2]
        else:
            desired_speed = self._waypoints[-1][2]
        self._desired_speed = desired_speed

    def update_waypoints(self, new_waypoints):
        self._waypoints = new_waypoints

    def get_commands(self):
        return self._set_throttle, self._set_steer, self._set_brake

    def set_throttle(self, input_throttle):
        # Clamp the throttle command to valid bounds
        throttle           = np.fmax(np.fmin(input_throttle, 1.0), 0.0)
        self._set_throttle = throttle

    def set_steer(self, input_steer_in_rad):
        # Covnert radians to [-1, 1]
        input_steer = self._conv_rad_to_steer * input_steer_in_rad

        # Clamp the steering command to valid bounds
        steer           = np.fmax(np.fmin(input_steer, 1.0), -1.0)
        self._set_steer = steer

    def set_brake(self, input_brake):
        # Clamp the steering command to valid bounds
        brake           = np.fmax(np.fmin(input_brake, 1.0), 0.0)
        self._set_brake = brake

    def update_controls(self):
        ######################################################
        # RETRIEVE SIMULATOR FEEDBACK
        ######################################################
        x               = self._current_x
        y               = self._current_y
        yaw             = self._current_yaw
        v               = self._current_speed
        self.update_desired_speed()
        v_desired       = self._desired_speed
        t               = self._current_timestamp
        waypoints       = self._waypoints
        throttle_output = 0
        steer_output    = 0
        brake_output    = 0

        ######################################################
        ######################################################
        # MODULE 7: DECLARE USAGE VARIABLES HERE
        ######################################################
        ######################################################
        """
            Use 'self.vars.create_var(<variable name>, <default value>)'
            to create a persistent variable (not destroyed at each iteration).
            This means that the value can be stored for use in the next
            iteration of the control loop.

            Example: Creation of 'v_previous', default value to be 0
            self.vars.create_var('v_previous', 0.0)

            Example: Setting 'v_previous' to be 1.0
            self.vars.v_previous = 1.0

            Example: Accessing the value from 'v_previous' to be used
            throttle_output = 0.5 * self.vars.v_previous
        """
        # self.vars.create_var('v_previous', 0.0)
        # self.vars.create_var('t_previous', 0.0)
        # self.vars.create_var('error_previous', 0.0)
        # self.vars.create_var('integral_error_previous', 0.0)
        # self.vars.create_var('throttle_previous', 0.0)

        #############
        self.vars.create_var('v_previous', 0.0)
        self.vars.create_var('t_previous', 0.0)
        self.vars.create_var('throttle_previous', 0.0)
        self.vars.create_var('int_val', 0.0)
        self.vars.create_var('last_error', 0.0)


        # Skip the first frame to store previous values properly
        if self._start_control_loop:
            """
                Controller iteration code block.

                Controller Feedback Variables:
                    x               : Current X position (meters)
                    y               : Current Y position (meters)
                    yaw             : Current yaw pose (radians)
                    v               : Current forward speed (meters per second)
                    t               : Current time (seconds)
                    v_desired       : Current desired speed (meters per second)
                                      (Computed as the speed to track at the
                                      closest waypoint to the vehicle.)
                    waypoints       : Current waypoints to track
                                      (Includes speed to track at each x,y
                                      location.)
                                      Format: [[x0, y0, v0],
                                               [x1, y1, v1],
                                               ...
                                               [xn, yn, vn]]
                                      Example:
                                          waypoints[2][1]: 
                                          Returns the 3rd waypoint's y position

                                          waypoints[5]:
                                          Returns [x5, y5, v5] (6th waypoint)
                
                Controller Output Variables:
                    throttle_output : Throttle output (0 to 1)
                    steer_output    : Steer output (-1.22 rad to 1.22 rad)
                    brake_output    : Brake output (0 to 1)
            """

            ######################################################
            ######################################################
            # MODULE 7: IMPLEMENTATION OF LONGITUDINAL CONTROLLER HERE
            ######################################################
            ######################################################
            """
                Implement a longitudinal controller here. Remember that you can
                access the persistent variables declared above here. For
                example, can treat self.vars.v_previous like a "global variable".
            """
            
            # Change these outputs with the longitudinal controller. Note that
            # brake_output is optional and is not required to pass the
            # assignment, as the car will naturally slow down over time.

            # throttle_output = 0
            # brake_output    = 0

            # # PID controller
            # Kp = 1.0
            # Ki = 1.0
            # Kd = 0.01

            # dt = t - self.vars.t_previous
            # e_v = v_desired - v
            # de_v = (e_v - self.vars.error_previous) / dt
            # inte_v = (e_v + self.vars.integral_error_previous) * dt

            # acc = Kp*e_v + Ki*inte_v + Kd*de_v

            # if acc > 0.0:
            #     throttle_output = (np.tanh(acc) + 1)/2
            #     if throttle_output - self.vars.throttle_previous > 0.1:
            #         throttle_output = self.vars.throttle_previous + 0.1
            #     else:
            #         throttle_output = 0



            # ######################################################
            # ######################################################
            # # MODULE 7: IMPLEMENTATION OF LATERAL CONTROLLER HERE
            # ######################################################
            # ######################################################
            # """
            #     Implement a lateral controller here. Remember that you can
            #     access the persistent variables declared above here. For
            #     example, can treat self.vars.v_previous like a "global variable".
            # """
            
            # # Change the steer output with the lateral controller. 
            # steer_output    = 0

            # Kdd = 0.1
            # ld_actual = 1.0
            # L = 2.9

            # # dx = [x - ix for ix in np.array(waypoints)[:, :1]]
            # # dy = [y - iy for iy in np.array(waypoints)[:, :2]]
            # # d = np.array(abs(np.sqrt(idx ** 2 + idy ** 2)) for (idx, idy) in zip(dx, dy))
            # # crosstrack_error = np.min(d)
            # # ind = int(min(np.where(d == crosstrack_error)))
            # # print(ind, d)
            # current_xy = np.array([x, y])
            # d = np.sqrt(np.sum((current_xy - np.array(waypoints)[:, :2])**2, axis=1))
            # crosstrack_error = np.min(d)
            # # ind = crosstrack_error.index()
            # ind = np.where(d == crosstrack_error)
            # ind = int(min(ind))

            # ld = Kdd*v + ld_actual
            # for i in range((ind+1), len(waypoints)):
            #     if d[i] >= ld:
            #         ind = i
            #         break

            # targetx = waypoints[ind][0]
            # targety = waypoints[ind][1]
            # print(d[ind])

            # ld = Kdd*v + ld_actual
            # alpha = np.arctan2((targety-y), (targetx-x)) - yaw
            # delta = np.arctan2(2.0*L*np.sin(alpha)/ld, 1.0)

            # # print(ind, crosstrack_error, delta)

            # yaw += v/L*np.tan(delta)*dt

            # expect_steer = min(1.22, yaw)
            # expect_steer = max(-1.22, yaw)

            # print(v, ind, crosstrack_error, delta, yaw, expect_steer)

            # steer_output = expect_steer

            #####################################
            kp = 1.0
            ki = 0.2
            kd = 0.01

            throttle_output = 0
            brake_output    = 0

            # pid control
            st = t - self.vars.t_previous

            # error term
            delta_v = v_desired - v

            # I
            integral = self.vars.int_val + delta_v * st

            # D
            derivate = (delta_v - self.vars.last_error) / st

            acc = kp * delta_v + ki * integral + kd * derivate

            if acc > 0:
                throttle_output = (np.tanh(acc) + 1)/2
                # throttle_output = max(0.0, min(1.0, throttle_output))
                if throttle_output - self.vars.throttle_previous > 0.1:
                    throttle_output = self.vars.throttle_previous + 0.1
            else:
                throttle_output = 0

            ######################################################
            ######################################################
            # MODULE 7: IMPLEMENTATION OF LATERAL CONTROLLER HERE
            ######################################################
            ######################################################
            """
                Implement a lateral controller here. Remember that you can
                access the persistent variables declared above here. For
                example, can treat self.vars.v_previous like a "global variable".
            """
            
            # Change the steer output with the lateral controller. 
            steer_output = 0

            # Use stanley controller for lateral control
            k_e = 0.3

            slope = (waypoints[-1][1]-waypoints[0][1])/ (waypoints[-1][0]-waypoints[0][0])
            a = -slope
            b = 1.0
            # c = (slope*waypoints[0][0]) - waypoints[0][1]

            # #heading error
            # yaw_diff_heading = np.arctan2(-a, b) - yaw
            # if yaw_diff_heading > np.pi:
            #     yaw_diff_heading -= 2*np.pi
            # if yaw_diff_heading < - np.pi:
            #     yaw_diff_heading += 2*np.pi
            yaw_path = np.arctan2(waypoints[-1][1]-waypoints[0][1], waypoints[-1][0]-waypoints[0][0])
            # yaw_path = np.arctan2(slope, 1.0)
            yaw_diff_heading = yaw_path - yaw 
            if yaw_diff_heading > np.pi:
                yaw_diff_heading -= 2 * np.pi
            if yaw_diff_heading < - np.pi:
                yaw_diff_heading += 2 * np.pi

            #cross track error
            # current_xy = np.array([x, y])
            # crosstrack_error = np.min(np.sum((current_xy - np.array(waypoints)[:, :2])**2, axis=1))

            # yaw_cross_track = np.arctan2(y-waypoints[0][1], x-waypoints[0][0])
            # yaw_path = np.arctan2(-a, b) - yaw_cross_track
            # if yaw_path > np.pi:
            #     yaw_path -= 2 * np.pi
            # if yaw_path < - np.pi:
            #     yaw_path += 2 * np.pi
            # if yaw_path > 0:
            #     crosstrack_error = abs(crosstrack_error)
            # else:
            #     crosstrack_error = - abs(crosstrack_error)

            # yaw_diff_crosstrack = np.arctan(k_e * crosstrack_error / (10+v))
            current_xy = np.array([x, y])
            crosstrack_error = np.min(np.sum((current_xy - np.array(waypoints)[:, :2])**2, axis=1))

            yaw_cross_track = np.arctan2(y-waypoints[0][1], x-waypoints[0][0])
            yaw_path2ct = yaw_path - yaw_cross_track
            if yaw_path2ct > np.pi:
                yaw_path2ct -= 2 * np.pi
            if yaw_path2ct < - np.pi:
                yaw_path2ct += 2 * np.pi
            if yaw_path2ct > 0:
                crosstrack_error = abs(crosstrack_error)
            else:
                crosstrack_error = - abs(crosstrack_error)

            yaw_diff_crosstrack = np.arctan(k_e * crosstrack_error / (v))

            steer_expect = yaw_diff_crosstrack + yaw_diff_heading

            # if steer_expect > np.pi:
            #     steer_expect -= 2 * np.pi
            # if steer_expect < - np.pi:
            #     steer_expect += 2 * np.pi
            # steer_expect = min(1.22, steer_expect)
            # steer_expect = max(-1.22, steer_expect)

            # steer_output = steer_expect
            if steer_expect > np.pi:
                steer_expect -= 2 * np.pi
            if steer_expect < - np.pi:
                steer_expect += 2 * np.pi
            steer_expect = min(1.22, steer_expect)
            steer_expect = max(-1.22, steer_expect)



            # # 1. calculate heading error
            # yaw_path = np.arctan2(waypoints[-1][1]-waypoints[0][1], waypoints[-1][0]-waypoints[0][0])
            # yaw_diff = yaw_path - yaw 
            # if yaw_diff > np.pi:
            #     yaw_diff -= 2 * np.pi
            # if yaw_diff < - np.pi:
            #     yaw_diff += 2 * np.pi

            # # 2. calculate crosstrack error
            # current_xy = np.array([x, y])
            # crosstrack_error = np.min(np.sum((current_xy - np.array(waypoints)[:, :2])**2, axis=1))

            # yaw_cross_track = np.arctan2(y-waypoints[0][1], x-waypoints[0][0])
            # yaw_path = yaw_path - yaw_cross_track
            # if yaw_path > np.pi:
            #     yaw_path -= 2 * np.pi
            # if yaw_path < - np.pi:
            #     yaw_path += 2 * np.pi
            # if yaw_path > 0:
            #     crosstrack_error = abs(crosstrack_error)
            # else:
            #     crosstrack_error = - abs(crosstrack_error)

            # yaw_diff_crosstrack = np.arctan(k_e * crosstrack_error / (k_v + v))
            
            # print (crosstrack_error, yaw_diff, yaw_diff_crosstrack)

            # # 3. control low
            # steer_expect = yaw_diff + yaw_diff_crosstrack
            # if steer_expect > np.pi:
            #     steer_expect -= 2 * np.pi
            # if steer_expect < - np.pi:
            #     steer_expect += 2 * np.pi
            # steer_expect = min(1.22, steer_expect)
            # steer_expect = max(-1.22, steer_expect)

            # # 4. update
            steer_output = steer_expect



            ######################################################
            # SET CONTROLS OUTPUT
            ######################################################
            self.set_throttle(throttle_output)  # in percent (0 to 1)
            self.set_steer(steer_output)        # in rad (-1.22 to 1.22)
            self.set_brake(brake_output)        # in percent (0 to 1)

        ######################################################
        ######################################################
        # MODULE 7: STORE OLD VALUES HERE (ADD MORE IF NECESSARY)
        ######################################################
        ######################################################
        """
            Use this block to store old values (for example, we can store the
            current x, y, and yaw values here using persistent variables for use
            in the next iteration)
        """
        self.vars.v_previous = v  # Store forward speed to be used in next step
        # self.vars.throttle_previous = throttle_output
        # self.vars.t_previous = t
        # self.vars.error_previous = e_v
        # self.vars.integral_error_previous = inte_v
        ##################
        self.vars.t_previous = t
        self.vars.int_val = integral
        self.vars.throttle_previous = throttle_output