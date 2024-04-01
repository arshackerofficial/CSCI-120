public class JobApplicant {
    private String name;
    private String phone;
    private boolean hasWordSkill;
    private boolean hasSpreadsheetSkill;
    private boolean hasDatabaseSkill;
    private boolean hasGraphicsSkill;

    public JobApplicant() {
        // This is the blank constructor
    }

    public JobApplicant(String name, String phone, boolean hasWordSkill, boolean hasSpreadsheetSkill, boolean hasDatabaseSkill, boolean hasGraphicsSkill) {
        this.name = name;
        this.phone = phone;
        this.hasWordSkill = hasWordSkill;
        this.hasSpreadsheetSkill = hasSpreadsheetSkill;
        this.hasDatabaseSkill = hasDatabaseSkill;
        this.hasGraphicsSkill = hasGraphicsSkill;
    }

    // Get methods for each field
    public String getName() {
        return this.name;
    }

    public String getPhone() {
        return this.phone;
    }

    public boolean getHasWordSkill() {
        return this.hasWordSkill;
    }

    public boolean getHasSpreadsheetSkill() {
        return this.hasSpreadsheetSkill;
    }

    public boolean getHasDatabaseSkill() {
        return this.hasDatabaseSkill;
    }

    public boolean getHasGraphicsSkill() {
        return this.hasGraphicsSkill;
    }
}
