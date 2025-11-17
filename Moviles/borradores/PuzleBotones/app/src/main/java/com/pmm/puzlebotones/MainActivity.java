package com.pmm.puzlebotones;

import android.annotation.SuppressLint;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.GridLayout;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private Button[][] botones = new Button[3][3];
    private int colorOriginal;
    private int colorSecundario;

    @SuppressLint("ResourceAsColor")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        colorOriginal= getColor(R.color.LTGRAY);
        colorSecundario = getColor(R.color.BLUE);

        
        GridLayout layout = new GridLayout(this);
        layout.setRowCount(4); 
        layout.setColumnCount(3);

        
        for (int fila = 0; fila < 3; fila++) {
            for (int col = 0; col < 3; col++) {
                Button b = new Button(this);
                b.setBackgroundColor(colorOriginal);

                GridLayout.LayoutParams params = new GridLayout.LayoutParams();
                params.rowSpec = GridLayout.spec(fila);
                params.columnSpec = GridLayout.spec(col);
                params.width = 250;
                params.height = 250;
                params.setMargins(8, 8, 8, 8);

                layout.addView(b, params);
                botones[fila][col] = b;

                int finalFila = fila;
                int finalCol = col;

                b.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        cambiarColor(finalFila, finalCol);
                        comprobarVictoria();
                    }
                });
            }
        }

        
        Button reiniciar = new Button(this);
        reiniciar.setText("Reiniciar");

        GridLayout.LayoutParams paramsReiniciar = new GridLayout.LayoutParams();
        paramsReiniciar.rowSpec = GridLayout.spec(3);
        paramsReiniciar.columnSpec = GridLayout.spec(0, 3); 
        paramsReiniciar.width = GridLayout.LayoutParams.MATCH_PARENT;
        paramsReiniciar.height = GridLayout.LayoutParams.WRAP_CONTENT;
        paramsReiniciar.setMargins(16, 16, 16, 16);

        reiniciar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                reiniciarJuego();
            }
        });

        layout.addView(reiniciar, paramsReiniciar);

        setContentView(layout);
    }


    private void cambiarColor(int fila, int col) {
        
        alternarColor(botones[fila][col]);

        
        if (fila > 0) alternarColor(botones[fila - 1][col]); 
        if (fila < 2) alternarColor(botones[fila + 1][col]); 
        if (col > 0) alternarColor(botones[fila][col - 1]); 
        if (col < 2) alternarColor(botones[fila][col + 1]); 
    }

    private void alternarColor(Button b) {
        int colorActual = ((ColorDrawable) b.getBackground()).getColor();
        if (colorActual == colorOriginal) {
            b.setBackgroundColor(colorSecundario);
        } else {
            b.setBackgroundColor(colorOriginal);
        }
    }

    private void comprobarVictoria() {
        for (int fila = 0; fila < 3; fila++) {
            for (int col = 0; col < 3; col++) {
                int colorActual = ((ColorDrawable) botones[fila][col].getBackground()).getColor();
                if (colorActual != colorSecundario) {
                    return; 
                }
            }
        }
        Toast.makeText(this, "¡Victoria! 🎉", Toast.LENGTH_LONG).show();
    }

    private void reiniciarJuego() {
        for (int fila = 0; fila < 3; fila++) {
            for (int col = 0; col < 3; col++) {
                botones[fila][col].setBackgroundColor(colorOriginal);
            }
        }
    }
}