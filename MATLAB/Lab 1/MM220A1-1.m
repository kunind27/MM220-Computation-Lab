%function plot1 (xmin, xmax, deltax, ymin,ymax, deltay)
xmin= -5*pi; xmax= 5*pi;
ymin= -5*pi; ymax= 5*pi;
deltax= pi/10 ;
deltay= pi/10;

%Defining The Grid
x1= xmin :deltax: xmax;
y1= ymin :deltay: ymax;
[x,y]= meshgrid(x1, y1);

%Defining Function z=f(x,y)
z= sin(x).*cos(y)./x;

%Testing what the meshgrid function does
%print(x1);
%print(x);

%Plotting Begins
surf(x,y,z);
xlabel('x');
ylabel('y');
zlabel('z= sin(x)cos(y)/x');  
print("plot1", "-dpng")
%end   

