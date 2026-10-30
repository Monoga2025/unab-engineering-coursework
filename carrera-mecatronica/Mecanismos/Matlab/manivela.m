clear all
clc

% Analisis de posicion mecanismo Manivela-Biela-Corredera centrado
% Longitudes de los eslabones
AB = 2.5; % Manivela
BC = 6; % Biela

for TETA2=0:360

    % Ecuaciones de posicion
    TETA3P = asind(AB*sind(TETA2)/BC);
    TETA3 = 180-TETA3P;
    AC = AB*cosd(TETA2)-BC*cosd(TETA3);

    % coordenadas de las juntas
    AX = 0;
    AY = 0;
    BX = AB*cosd(TETA2);
    BY = AB*sind(TETA2);
    CX = AC;
    CY = 0;

    % Crear los vectores a graficar
    X = [AX BX CX];
    Y = [AY BY CY];

    subplot(2,1,1)
    plot(X,Y,'-o','LineWidth',2);
    hold on

    vc = [CX CY]; % Vector de coordenadas de C
    va = [AX AY]; % Vector de coordenadas de A
    vb = [BX BY]; % Vector de coordenadas de B

    C_circ = viscircles(vc,0.1); % Dibujo de circulos
    A_circ = viscircles(va,0.1); % Dibujo de circulos
    B_circ = viscircles(vb,0.1); % Dibujo de circulos

    Trayectoria = viscircles([0,0],AB,'LineStyle','--'); % Trayectoria del punto B
    % 


    if TETA2==30 || TETA2==180 || TETA2==210
        fprintf('\nSi TETA  = %.2f', TETA2);
        fprintf('\nTETA 3 = %.2f', TETA3);
        fprintf('\nAC = %.2f', AC);
        fprintf('\nCX = %.2f', CX);
        fprintf('\nCY = %.2f', CY);
        fprintf('\n');
    end

    axis equal
    axis([-AB-1 AB+BC+1 -AB-1 AB+1])

    pause(0.01)

    delete(A_circ);
    delete(B_circ);
    delete(C_circ);
    delete(Trayectoria);

    hold off

    subplot(2,1,2)
    plot(TETA2,CX,'--rs','LineWidth',2)
    title('Posicion CX vs TETA2')
    hold on

end
