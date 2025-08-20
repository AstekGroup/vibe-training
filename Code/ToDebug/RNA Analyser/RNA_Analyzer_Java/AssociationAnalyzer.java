import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class AssociationAnalyzer {

    private static final String CSV_FILE_PATH = "/Users/philippe.pary/Documents/Formations/Vibe coding/Code/ToDebug/RNA Analyser/bdd_asso_rna.csv";
    private static final String DELIMITER = ";"; // Changed to String for split method
    private static final int OBJET_COLUMN_INDEX = 13;      
    private static final int ADRS_CODEPOSTAL_COLUMN_INDEX = 23;
    private static final int PROGRESS_UPDATE_INTERVAL = 100000; // Update every 100,000 lines

    public static void main(String[] args) {
        Map<String, Integer> associationsPerDepartment = new HashMap<>();
        int emptyObjetCount = 0;
        long totalLines = 0;

        // First pass to count total lines for progress indication
        System.out.println("Counting total lines...");
        try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE_PATH))) {
            while (br.readLine() != null) {
                totalLines++;
            }
            // Subtract 1 for the header line
            if (totalLines > 0) totalLines--; 
        } catch (IOException e) {
            System.err.println("Error counting lines in CSV file: " + e.getMessage());
            return;
        }

        System.out.println("Total lines to process: " + totalLines);
        long startTime = System.currentTimeMillis();
        long linesProcessed = 0;

        try (BufferedReader br = new BufferedReader(new FileReader(CSV_FILE_PATH))) {
            // Skip header line
            br.readLine(); 
            String line;
            while ((line = br.readLine()) != null) {
                linesProcessed++;
                String department = "";
                String objet = "";
                
                String[] fields = line.split(DELIMITER, -1); // -1 to keep trailing empty strings

                if (fields.length > ADRS_CODEPOSTAL_COLUMN_INDEX) {
                    String codePostal = fields[ADRS_CODEPOSTAL_COLUMN_INDEX].trim();
                    if (codePostal.length() >= 2) {
                        // Ensure the extracted part is numeric before taking the first two digits
                        if (codePostal.matches("\\d+")) {
                            department = codePostal.substring(0, 2);
                        }
                    }
                }

                if (fields.length > OBJET_COLUMN_INDEX) {
                    objet = fields[OBJET_COLUMN_INDEX].trim();
                    if (objet.isEmpty()) {
                        emptyObjetCount++;
                    }
                }

                if (!department.isEmpty()) {
                    associationsPerDepartment.put(department, associationsPerDepartment.getOrDefault(department, 0) + 1);
                }

                if (linesProcessed % PROGRESS_UPDATE_INTERVAL == 0) {
                    double progress = (double) linesProcessed / totalLines * 100;
                    System.out.printf("Processing... %.2f%% (%,d lines)%n", progress, linesProcessed);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading the CSV file: " + e.getMessage());
            return;
        }

        long endTime = System.currentTimeMillis();
        System.out.println("\nAnalysis completed in " + (endTime - startTime) + " ms");
        System.out.println("Number of associations per department:");
        for (Map.Entry<String, Integer> entry : associationsPerDepartment.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        System.out.println("\nNumber of associations with empty objet: " + emptyObjetCount);
    }
}