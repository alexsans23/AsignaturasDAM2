package com.naciones.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Country {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer countryId;

    private String name;
    private Double area;
    private String countryCode2;
    private String countryCode3;

    public Country() {
    	
    }

    public Country(String name, Double area, String countryCode2, String countryCode3) {
        this.name = name;
        this.area = area;
        this.countryCode2 = countryCode2;
        this.countryCode3 = countryCode3;
    }

    // Getters y setters
    public Integer getCountryId() { 
    	return countryId; 
    	}
    
    public void setCountryId(Integer countryId) {
    	this.countryId = countryId; 
    	}

    public String getName() {
    	return name; 
    	}
    
    public void setName(String name) {
    	this.name = name; 
    	}

    public Double getArea() {
    	return area; 
    	}
    
    public void setArea(Double area) {
    	this.area = area; 
    	}

    public String getCountryCode2() {
    	return countryCode2; 
    	}
    
    public void setCountryCode2(String countryCode2) {
    	this.countryCode2 = countryCode2; 
    	}

    public String getCountryCode3() {
    	return countryCode3; 
    	}
    
    public void setCountryCode3(String countryCode3) {
    	this.countryCode3 = countryCode3; 
    	}

    @Override
    public String toString() {
        return "Country{" +
                "countryId=" + countryId +
                ", name='" + name + '\'' +
                ", area=" + area +
                ", code2='" + countryCode2 + '\'' +
                ", code3='" + countryCode3 + '\'' +
                '}';
    }
}
