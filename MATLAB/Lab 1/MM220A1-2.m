u= 30;
g= 9.8;
deltat= 0.1;
t1= [0:deltat:15];
h1= u*t1 -0.5*g*(t1.^2);

hmax=0; %Initially
tmax=0;

%Loop for Calculating Max Height and Time of Flight
for i= 1:length(h1)
    if hmax<= h1(i)
        hmax=h1(i);
    end
    if ((h1(i)>0 && h1(i+1)<0) || (h1(i)==0))
        tmax= t1(i);
    end
end

%Displaying the Max Height and Max Time Elapsed
disp(hmax);
disp(tmax);

%Initializing Arrays for Submission to be used for PLotting
t= [0:deltat:tmax];
h= u*t -0.5*g*t.^2;

%Plotting Begins
plot(t, h, 'Color', 'magenta');
xlim([0, tmax]);
xlabel("Time Elapsed (s)");
ylabel("Height of projectile (m)");
print("plot2","-dpng");

