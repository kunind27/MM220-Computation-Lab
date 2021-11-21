tau= 1236;
n=4.2;
time=[300,540,660,780,960,1080,1260,1440,1620,1800];
fraction=[0.039,0.050,0.065,0.108,0.285,0.458,0.661,0.857,0.935,0.967];

syms t; %Declaring symbolic variables f and t

%Integrating using EXPLICIT FORMULATION
eqn1=' Df = (n*(t^(n-1))/( tau^n)) * exp(-(t/tau)^n)';
ic='f(0)=0'; %Initial Condition 
f1= dsolve(eqn1, ic);

%Converting symbolic equation to MATLAB Operable equation
t=[0:1:1800];
f_explicit= subs(f1);
plot(t, f_explicit, 'Color', 'green');
hold on;

%Integrating using ODE45 Runge Kutta Formulation (Numerical Way)
%No need for symbolic variable declaration, but f,t will be vectors
dfdt= @(t,f) (n*(t.^(n-1)))/(tau^n) .* exp(-(t/tau).^n);
tspan=[0 1800];
f0=0; %Initial Condition
[t, f_numerical]=ode45(dfdt, tspan, f0);

%Plotting begins
plot(t, f_numerical, "Color", 'r');
plot(time, fraction, "*", 'Color', 'b');
legend('Explicit sol^n', 'Numerical sol^n', "Expt Data");
xlabel('t');
ylabel('Fraction of alloy transformed (f)');
hold off;
print("MM220A3",'-dpng');