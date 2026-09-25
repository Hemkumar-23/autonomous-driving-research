% Day 27 - Software-in-the-Loop vehicle dynamics
% Implements the same simplified longitudinal model used in Day 26.

clear;
clc;

% Vehicle parameters
m = 1000;          % vehicle mass [kg]
F_drive = 2000;    % driving force [N]
F_resist = 0;      % resistive force [N]

% Simulation parameters
dt = 0.01;         % simulation step [s]
t_end = 10;        % simulation duration [s]
t = 0:dt:t_end;

% Initial conditions
v = zeros(size(t));    % velocity [m/s]
x = zeros(size(t));    % position [m]
a = zeros(size(t));    % acceleration [m/s^2]

% SIL simulation
for k = 1:length(t)-1

    % Vehicle longitudinal dynamics
    a(k) = (F_drive - F_resist) / m;

    % Integrate acceleration to velocity
    v(k+1) = v(k) + a(k) * dt;

    % Integrate velocity to position
    x(k+1) = x(k) + v(k) * dt;

end

% Final acceleration value
a(end) = a(end-1);

% Display results
fprintf('SIL Results:\n');
fprintf('Final acceleration: %.2f m/s^2\n', a(end));
fprintf('Final velocity:     %.2f m/s\n', v(end));
fprintf('Final position:     %.2f m\n', x(end));

% Plot results
figure;

subplot(3,1,1);
plot(t,a);
grid on;
ylabel('Acceleration [m/s^2]');
title('SIL Vehicle Dynamics');

subplot(3,1,2);
plot(t,v);
grid on;
ylabel('Velocity [m/s]');

subplot(3,1,3);
plot(t,x);
grid on;
ylabel('Position [m]');
xlabel('Time [s]');
