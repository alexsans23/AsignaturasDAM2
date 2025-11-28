package com.example.blue;

import android.bluetooth.BluetoothAdapter;
import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    BluetoothAdapter BTAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        BTAdapter = BluetoothAdapter.getDefaultAdapter();

        if(BTAdapter == null) {
            Toast.makeText(this, "el disposdditovo carece de blue", Toast.LENGTH_SHORT).show();
        }else{
            if (BTAdapter.isEnabled()){
                Intent enableBIntent =  new Intent(BluetoothAdapter.ACTION)

            }
        }

    }
}