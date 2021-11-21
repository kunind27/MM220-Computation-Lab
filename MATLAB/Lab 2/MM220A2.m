function [coeffs10, coeffs20, stress10, stress20, error10, error20]= MM220A1()
    A= importdata("exp_stress_strain.txt")
    stress= A(:,2)';
    total_strain= A(:,1)';
    
    %Sample Size 
    [m,n]= size(stress);
    
    Y= 330000; %Young's Modulus In MPa
    
    elastic_strain= stress/Y;
    plastic_strain= total_strain - elastic_strain;
    
   
    %Polynomial Fitting begins, degree= 10 and 20
    coeffs10= polyfit(plastic_strain, stress, 10);
    coeffs20= polyfit(plastic_strain, stress, 20);
    
    %Calculating Stress from 2 Fits
    stress10= polyval(coeffs10, plastic_strain);
    stress20= polyval(coeffs20, plastic_strain);
    
    %Total Strain from Poly Fitting
    total_strain10= plastic_strain + stress10/Y;
    total_strain20= plastic_strain + stress20/Y;
    
   
    %Plotting Begins
    plot(total_strain, stress, 'o', 'LineWidth',4, 'Color','b');
    hold on;
    plot(total_strain10, stress10, 'Color', 'r');
    plot(total_strain20, stress20, "Color", 'g');
   
    %Adding Axes Labels and Legend
    xlabel("Total Strain");
    ylabel("Stress");
    legend("Stress Expt", "Stress10", "Stress20");
    
    
    %Calculating Error
    error10= sqrt( sum(((stress10- stress)./stress).^2)/n );
    error20= sqrt( sum(((stress20-stress)./stress).^2)/n  );

    disp(error10);
    disp(error20);
    
    %Saving the Plot
    print("MM220A1", "-dpng");
end