package com.revolvingmadness.pythonmc.pythonmclibrary;

public enum PyTime {
    DAY, MIDNIGHT, NIGHT, NOON;

    public long toTimeLong() {
        return switch (this) {
            case DAY -> 1000;
            case MIDNIGHT -> 18000;
            case NIGHT -> 13000;
            case NOON -> 6000;
        };
    }
}
