package com.pmm.a22; // Asegúrate de que coincide exactamente con tu paquete real

import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.pmm.a22.calculator.Calculator;

public class MainActivity extends AppCompatActivity {

    private final Calculator _calculator = new Calculator();

    private String resultado = "";
    private boolean calculado = false;

    private TextView tvOperation;
    private TextView tvResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_calculator);

        // Ajuste opcional para evitar que la interfaz se tape con la barra de estado
        try {
            ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
                Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
                v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
                return insets;
            });
        } catch (Exception ignored) {}

        tvOperation = findViewById(R.id.tv_operation);
        tvResult = findViewById(R.id.tv_result);

        updateDisplay();
    }

    // -----------------------------------
    // BOTONES NUMÉRICOS (0–9 y .)
    // -----------------------------------
    public void operandClick(View view) {
        if (calculado) clearClick(null);

        int id = view.getId();
        String operand = "";

        if (id == R.id.btn_0) operand = "0";
        else if (id == R.id.btn_1) operand = "1";
        else if (id == R.id.btn_2) operand = "2";
        else if (id == R.id.btn_3) operand = "3";
        else if (id == R.id.btn_4) operand = "4";
        else if (id == R.id.btn_5) operand = "5";
        else if (id == R.id.btn_6) operand = "6";
        else if (id == R.id.btn_7) operand = "7";
        else if (id == R.id.btn_8) operand = "8";
        else if (id == R.id.btn_9) operand = "9";
        else if (id == R.id.btn_dot) operand = ".";
        else return;

        _calculator.setOperand(operand);
        resultado += operand;
        updateDisplay();
    }

    // -----------------------------------
    // OPERADORES (+ - * /)
    // -----------------------------------
    public void operatorClick(View view) {
        int id = view.getId();
        Calculator.Operators operator = null;

        // Si ya hay una operación en curso, calculamos primero
        if (!_calculator.isNewOperation()) {
            try {
                Float calcRes = _calculator.calculate();
                resultado = stripTrailingZeros(calcRes);
                calculado = true;
                _calculator.clear();

                // Usar el resultado como nuevo primer operando
                for (char c : resultado.toCharArray()) {
                    _calculator.setOperand(String.valueOf(c));
                }
                updateDisplay();
            } catch (Calculator.MissingOperandException e) {
                Toast.makeText(this, "Falta un operando", Toast.LENGTH_SHORT).show();
                return;
            } catch (Calculator.DivisionByZeroException e) {
                Toast.makeText(this, "Error: división por 0", Toast.LENGTH_SHORT).show();
                return;
            }
        }

        if (id == R.id.btn_add) operator = Calculator.Operators.ADD;
        else if (id == R.id.btn_sub) operator = Calculator.Operators.SUBSTRACT;
        else if (id == R.id.btn_mul) operator = Calculator.Operators.MULTIPLY;
        else if (id == R.id.btn_div) operator = Calculator.Operators.DIVIDE;
        else return;

        _calculator.setOperator(operator);
        resultado += operator.toString();
        updateDisplay();
    }

    // -----------------------------------
    // BOTÓN "="
    // -----------------------------------
    public void equalsClick(View view) {
        try {
            Float calcRes = _calculator.calculate();
            resultado = stripTrailingZeros(calcRes);
            calculado = true;
            updateDisplay();
        } catch (Calculator.MissingOperandException e) {
            Toast.makeText(this, "Falta un operando", Toast.LENGTH_SHORT).show();
        } catch (Calculator.DivisionByZeroException e) {
            Toast.makeText(this, "Error: división por 0", Toast.LENGTH_SHORT).show();
        } catch (NumberFormatException e) {
            Toast.makeText(this, "Número no válido", Toast.LENGTH_SHORT).show();
        }
    }

    // -----------------------------------
    // BOTÓN "C" (clear)
    // -----------------------------------
    public void clearClick(View view) {
        _calculator.clear();
        calculado = false;
        resultado = "";
        updateDisplay();
    }

    // -----------------------------------
    // ACTUALIZAR LA PANTALLA
    // -----------------------------------
    private void updateDisplay() {
        if (calculado) {
            tvOperation.setText("");
            tvResult.setText(resultado.isEmpty() ? "0" : resultado);
        } else {
            tvOperation.setText(resultado);
            tvResult.setText(resultado.isEmpty() ? "0" : resultado);
        }
    }

    // -----------------------------------
    // ELIMINA EL ".0" SI ES ENTERO
    // -----------------------------------
    private String stripTrailingZeros(Float val) {
        if (val == null) return "";
        if (val == val.longValue()) return String.valueOf(val.longValue());
        return String.valueOf(val);
    }
}
