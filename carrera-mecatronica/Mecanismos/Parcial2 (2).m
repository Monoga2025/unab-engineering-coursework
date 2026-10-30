clear all
close all
clc
% Analisis de posicion mecanismo de 6 eslabones
% Longitudes de los eslabones
a = 2; % O2A
b = 8; % AC
d = 4; % AB
f = 4; % BD
g = 4; % DO6
h = 5; % O2O6

for TETA2=0:360

    % Ecuaciones de posicion primer lazo
    % R2 - R3 - R1 = 0

    TETA3       = 180-asind((a*sind(TETA2))/b);

    Cx          = a*cosd(TETA2)-b*cosd(TETA3);


    % Ecuaciones de posicion segundo lazo
    % R2 - R4 + R5 - R6 - R7 = 0

    P           = -a*cosd(TETA2)+d*cosd(TETA3);

    Q           = -a*sind(TETA2)+d*sind(TETA3)+h;

    K           = ((f^2)-(P^2)-(Q^2)-(g^2))/(2*g);

    R           = sqrt((P^2)+(Q^2));

    PHI         = atan2d(Q,P);

    ALFA        = acosd(K/R);

    TETA6       = PHI-ALFA;

    if TETA6<0
        TETA6 = TETA6+360;
    end

    TETA5       = acosd((g*cosd(TETA6)-a*cosd(TETA2)+d*cosd(TETA3))/f);


    % Coordenadas de las juntas
    O2X         = 0;
    O2Y         = 0;

    O6X         = 0;
    O6Y         = h;

    AX          = a*cosd(TETA2);
    AY          = a*sind(TETA2);

    BX          = AX-d*cosd(TETA3);
    BY          = AY-d*sind(TETA3);

    CX          = Cx;
    CY          = 0;

    DX          = BX+f*cosd(TETA5);
    DY          = BY+f*sind(TETA5);


    % Crear los vectores a graficar
    X           = [O2X AX BX CX];
    Y           = [O2Y AY BY CY];

    X2          = [BX DX O6X];
    Y2          = [BY DY O6Y];


    subplot(2,1,1)
    plot(X,Y);
    hold on
    plot(X2,Y2);

      vo2 = [O2X O2Y]; % Vector coordenada de O2
      va = [AX AY]; % Vector coordenada de A
      vb = [BX BY]; % Vector coordenada de B
      vc = [CX CY]; % Vector coordenada de C
      vd = [DX DY]; % Vector coordenada de D
      vo6 = [O6X O6Y]; % Vector coordenada de O6

     O2_circ = viscircles(vo2,0.1); % Dibujo de circulos
     A_circ = viscircles(va,0.1); % Dibujo de circulos
     B_circ = viscircles(vb,0.1); % Dibujo de circulos
     C_circ = viscircles(vc,0.1); % Dibujo de circulos
     D_circ = viscircles(vd,0.1); % Dibujo de circulos
     O6_circ = viscircles(vo6,0.1); % Dibujo de circulos

     A_traj = viscircles([0 0],a,'LineStyle','--'); % Trayectoria del Punto A


     if TETA2==74 || TETA2==147 || TETA2==230 || TETA2==285

         fprintf('\nSi TETA 2 = %.2f grados', TETA2);
         fprintf('\nTETA 3 = %.2f grados', TETA3);
         fprintf('\nCx = %.2f in', CX);
         fprintf('\nTETA 5 = %.2f grados', TETA5);
         fprintf('\nTETA 6 = %.2f grados', TETA6);
         fprintf('\n--------------------------');

     end


axis equal
axis([-4 10 -3 8]);
pause(0.01)

 delete(O2_circ);
 delete(A_circ);
 delete(B_circ);
 delete(C_circ);
 delete(D_circ);
 delete(O6_circ);

 hold off


 subplot(2,1,2)
 plot(TETA2,CX,'--rs','LineWidth',2)
 title('Posicion Cx vs TETA2')
 hold on

end